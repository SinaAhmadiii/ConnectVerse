from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
    path('profile/<int:user_id>/', views.profile_detail, name='profile_detail'),
]
