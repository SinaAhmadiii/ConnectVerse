from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Profile

def view_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    
    context = {'profile': profile}
    return render(request, 'profile/view_profile.html', context)

def edit_profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    
    if request.method == 'POST':
        bio = request.POST.get('bio')
        profile.bio = bio
        profile.save()
        return redirect('view_profile', username=user.username)
    
    context = {'profile': profile}
    return render(request, 'profile/edit_profile.html', context)

def update_profile_picture(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    
    if request.method == 'POST':
        profile_picture = request.FILES.get('profile_picture')
        profile.profile_picture = profile_picture
        profile.save()
        return redirect('view_profile', username=user.username)
    
    context = {'profile': profile}
    return render(request, 'profile/update_profile_picture.html', context)

def delete_profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    
    if request.method == 'POST':
        profile.delete_profile()
        return redirect('home')
    
    context = {'profile': profile}
    return render(request, 'profile/delete_profile.html', context)
