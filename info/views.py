from django.shortcuts import render
from .models import Profile

def profile_detail(request, user_id):
    profile = Profile.objects.get(user_id=user_id)
    return render(request, 'profile_detail.html', {'profile': profile})
