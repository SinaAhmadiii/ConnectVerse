from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from .models import User


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User


class UserPasswordResetForm(PasswordResetForm):
    class Meta:
        model = User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'age', 'phone_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = 'The unique username for the user.'
        self.fields['first_name'].help_text = 'The user\'s first name.'
        self.fields['last_name'].help_text = 'The user\'s last name.'
        self.fields['email'].help_text = 'The unique email address for the user.'
        self.fields['age'].help_text = 'The age of the user (optional).'
        self.fields['phone_number'].help_text = 'The phone number of the user (optional).'


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'age', 'phone_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].help_text = 'The unique email address for the user.'
        self.fields['age'].help_text = 'The age of the user (optional).'
        self.fields['phone_number'].help_text = 'The phone number of the user (optional).'
