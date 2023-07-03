from django.urls import path
from .views import ReplyListView, ReplyCreateView, ReplyUpdateView, ReplyDeleteView

urlpatterns = [
    path('replies/', ReplyListView.as_view(), name='reply-list'),
    path('replies/create/', ReplyCreateView.as_view(), name='reply-create'),
    path('replies/<int:pk>/update/', ReplyUpdateView.as_view(), name='reply-update'),
    path('replies/<int:pk>/delete/', ReplyDeleteView.as_view(), name='reply-delete'),
]
