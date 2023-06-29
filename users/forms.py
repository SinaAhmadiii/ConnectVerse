from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'age', 'phone_number']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'phone_number': 'Phone Number',
        }
        help_texts = {
            'username': 'The unique username for the user.',
            'email': 'The unique email address for the user.',
            'first_name': 'The user\'s first name.',
            'last_name': 'The user\'s last name.',
            'age': 'The age of the user (optional).',
            'phone_number': 'The phone number of the user (optional).',
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'age', 'phone_number']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'phone_number': 'Phone Number',
        }
        help_texts = {
            'username': 'The unique username for the user.',
            'email': 'The unique email address for the user.',
            'first_name': 'The user\'s first name.',
            'last_name': 'The user\'s last name.',
            'age': 'The age of the user (optional).',
            'phone_number': 'The phone number of the user (optional).',
        }


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class UserPasswordChangeForm(forms.Form):
    current_password = forms.CharField(label='Current Password', widget=forms.PasswordInput)
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_new_password = cleaned_data.get('confirm_new_password')

        if new_password and confirm_new_password and new_password != confirm_new_password:
            raise forms.ValidationError('The new password and confirm new password do not match.')

        return cleaned_data


class UserPasswordResetForm(forms.Form):
    email = forms.EmailField(label='Email')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('No user with this email address exists.')

        return email
