from django.urls import path
from .views import (
    UserRegistrationView,
    UserLoginView,
    UserLogoutView,
    UserDashboardView,
    UserUpdateView,
    UserPasswordChangeView,
    UserPasswordResetView,
    UserPasswordResetDoneView,
    UserPasswordResetConfirmView,
    UserPasswordResetCompleteView,
    UserListView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView,
)

app_name = 'users'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('dashboard/', UserDashboardView.as_view(), name='dashboard'),
    path('update-profile/', UserUpdateView.as_view(), name='update_profile'),
    path('change-password/', UserPasswordChangeView.as_view(), name='change_password'),
    path('password-reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('user-list/', UserListView.as_view(), name='user_list'),
    path('user-create/', UserCreateView.as_view(), name='user_create'),
    path('user-update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user-delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]
