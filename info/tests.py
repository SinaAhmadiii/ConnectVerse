from django.test import RequestFactory
from django.urls import reverse
import pytest
from .models import Profile
from .views import profile_detail

@pytest.mark.django_db
def test_profile_detail_view():
    profile = Profile.objects.create(user_id=1, profile_picture='profile.jpg', bio='Test Bio')

    request = RequestFactory().get(reverse('info:profile_detail', args=[profile.user_id]))

    response = profile_detail(request, user_id=profile.user_id)

    assert response.status_code == 200

    assert 'profile' in response.context

    assert 'info/profile_detail.html' in response.template_name
