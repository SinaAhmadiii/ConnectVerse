from django.urls import path
from . import views

app_name = 'reply'

urlpatterns = [
    path('reply/<int:reply_id>/', views.reply_detail, name='reply_detail'),
    path('comment/<int:comment_id>/replies/', views.comment_replies, name='comment_replies'),
]
