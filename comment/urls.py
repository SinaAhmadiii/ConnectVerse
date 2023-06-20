from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    path('comment/<int:comment_id>/', views.comment_detail, name='comment_detail'),
]
