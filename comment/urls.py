from django.urls import path
from .views import CommentListView, CommentCreateView, CommentUpdateView, CommentDeleteView

app_name = 'comment'

urlpatterns = [
    path('', CommentListView.as_view(), name='comment_list'),
    path('create/', CommentCreateView.as_view(), name='comment_create'),
    path('update/<int:pk>/', CommentUpdateView.as_view(), name='comment_update'),
    path('delete/<int:pk>/', CommentDeleteView.as_view(), name='comment_delete'),
]
