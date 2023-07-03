from django.urls import path
from .views import (
    ProfileCreateView,
    ProfileUpdateView,
    BioUpdateView,
    ProfileDeleteView,
    ProfileDetailView,
)

app_name = 'info'

urlpatterns = [
    path('profile/create/', ProfileCreateView.as_view(), name='profile_create'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('bio/update/', BioUpdateView.as_view(), name='bio_update'),
    path('profile/delete/', ProfileDeleteView.as_view(), name='profile_delete'),
    path('profile/', ProfileDetailView.as_view(), name='profile_detail'),
]
