from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    FormView,
    TemplateView,
    UpdateView,
    ListView,
    CreateView,
    DeleteView,
)
from django.shortcuts import redirect

from .forms import (
    UserRegistrationForm,
    UserLoginForm,
    UserPasswordChangeForm,
    UserPasswordResetForm,
    UserUpdateForm,
)
from .models import User


class UserRegistrationView(FormView):
    template_name = 'registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserLoginView(FormView):
    template_name = 'login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)

        form.add_error(None, 'Invalid username or password')
        return super().form_invalid(form)


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'update_profile.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChangeView(LoginRequiredMixin, FormView):
    template_name = 'change_password.html'
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = self.request.user
        current_password = form.cleaned_data['current_password']
        new_password = form.cleaned_data['new_password']

        if user.check_password(current_password):
            user.set_password(new_password)
            user.save()
            return super().form_valid(form)

        form.add_error('current_password', 'Incorrect current password')
        return super().form_invalid(form)


class UserPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    form_class = UserPasswordResetForm
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'


class UserCreateView(CreateView):
    model = User
    template_name = 'user_create.html'
    fields = ['first_name', 'last_name', 'username', 'email', 'age', 'phone_number']
    success_url = reverse_lazy('user_list')


class UserUpdateView(UpdateView):
    model = User
    template_name = 'user_update.html'
    fields = ['first_name', 'last_name', 'username', 'email', 'age', 'phone_number']
    success_url = reverse_lazy('user_list')


class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('user_list')
