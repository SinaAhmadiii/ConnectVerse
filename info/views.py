from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from .forms import ProfilePictureForm, BioForm, DeleteProfileForm
from .models import Profile

class ProfileCreateView(CreateView):
    model = Profile
    template_name = 'profile_create.html'
    fields = ['profile_picture', 'bio']

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Profile created successfully.')
        return super().form_valid(form)

class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'profile_update.html'
    form_class = ProfilePictureForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bio_form'] = BioForm(instance=self.object)
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Profile picture updated successfully.')
        return super().form_valid(form)

class BioUpdateView(UpdateView):
    model = Profile
    template_name = 'bio_update.html'
    form_class = BioForm

    def form_valid(self, form):
        messages.success(self.request, 'Bio updated successfully.')
        return super().form_valid(form)

class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profile_delete.html'
    success_url = '/home/'
    context_object_name = 'profile'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Profile deleted successfully.')
        return super().delete(request, *args, **kwargs)

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile_detail.html'
    context_object_name = 'profile'

