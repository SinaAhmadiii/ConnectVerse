from django.urls import path
from .views import BookmarkListView, BookmarkCreateView, BookmarkUpdateView, BookmarkDeleteView

app_name = 'bookmark'

urlpatterns = [
    path('', BookmarkListView.as_view(), name='bookmark_list'),
    path('create/', BookmarkCreateView.as_view(), name='bookmark_create'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='bookmark_update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='bookmark_delete'),
]
