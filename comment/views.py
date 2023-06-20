from django.shortcuts import render
from .models import Comment

def comment_detail(request, comment_id):
    comment = Comment.objects.get(comment_id=comment_id)
    return render(request, 'comment_detail.html', {'comment': comment})
