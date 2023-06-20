from django.urls import path
from . import views

app_name = 'bookmark'

urlpatterns = [
    path('', views.bookmark_list, name='bookmark_list'),
    path('detail/<int:bookmark_id>/', views.bookmark_detail, name='bookmark_detail'),
    path('post/<int:post_id>/', views.bookmark_post, name='bookmark_post'),
    path('remove/<int:bookmark_id>/', views.remove_bookmark, name='remove_bookmark'),
]
