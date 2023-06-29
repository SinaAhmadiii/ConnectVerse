from django import forms
from django.core.exceptions import ValidationError
from .models import Profile


class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']

    def save(self, commit=True):
        profile = super().save(commit=False)
        if commit:
            profile.save()
        return profile


class BioForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']

    def save(self, commit=True):
        profile = super().save(commit=False)
        if commit:
            profile.save()
        return profile


class DeleteProfileForm(forms.ModelForm):
    confirm_username = forms.CharField(label="Confirm Username", max_length=150)

    class Meta:
        model = Profile
        fields = []

    def clean_confirm_username(self):
        confirm_username = self.cleaned_data.get('confirm_username')
        if confirm_username != self.instance.user.username:
            raise ValidationError("The entered username does not match.")
        return confirm_username

    def save(self, commit=True):
        profile = self.instance
        user = profile.user
        if commit:
            user.delete()
            profile.delete()
        return profile
