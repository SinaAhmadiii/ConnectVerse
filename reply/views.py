from django.shortcuts import render, get_object_or_404
from .models import Reply
from comment.models import Comment

def reply_detail(request, reply_id):
    reply = get_object_or_404(Reply, reply_id=reply_id)
    return render(request, 'reply_detail.html', {'reply': reply})

def comment_replies(request, comment_id):
    comment = get_object_or_404(Comment, comment_id=comment_id)
    replies = Reply.objects.filter(comment=comment)
    return render(request, 'comment_replies.html', {'comment': comment, 'replies': replies})
