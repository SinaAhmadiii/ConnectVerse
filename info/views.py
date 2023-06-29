from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from .forms import ProfilePictureForm, BioForm, DeleteProfileForm

from .models import Profile


class ProfileUpdateView(View):
    def get(self, request):
        profile = request.user.profile
        picture_form = ProfilePictureForm(instance=profile)
        bio_form = BioForm(instance=profile)
        context = {
            'picture_form': picture_form,
            'bio_form': bio_form
        }
        return render(request, 'profile_update.html', context)

    def post(self, request):
        profile = request.user.profile
        picture_form = ProfilePictureForm(request.POST, request.FILES, instance=profile)
        bio_form = BioForm(request.POST, instance=profile)

        if picture_form.is_valid():
            picture_form.save()
            messages.success(request, 'Profile picture updated successfully.')

        if bio_form.is_valid():
            bio_form.save()
            messages.success(request, 'Bio updated successfully.')

        return redirect('profile')


class ProfileDeleteView(View):
    def get(self, request):
        form = DeleteProfileForm()
        return render(request, 'profile_delete.html', {'form': form})

    def post(self, request):
        form = DeleteProfileForm(request.POST, instance=request.user.profile)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile deleted successfully.')
            return redirect('home')

        return render(request, 'profile_delete.html', {'form': form})


class ProfileDetailView(View):
    def get(self, request):
        profile = request.user.profile
        context = {
            'profile': profile
        }
        return render(request, 'profile_detail.html', context)
