from django.shortcuts import render, get_object_or_404, redirect
from comment.models import Comment
from .models import Reply

def create_reply(request, comment_id):
    comment = get_object_or_404(Comment, comment_id=comment_id)
    
    if request.method == 'POST':
        reply_text = request.POST.get('reply_text')
        reply = Reply(user=request.user, comment=comment, reply_text=reply_text)
        reply.save()
        return redirect('comment_detail', comment_id=comment_id)
    
    context = {'comment': comment}
    return render(request, 'reply/create_reply.html', context)

def edit_reply(request, reply_id):
    reply = get_object_or_404(Reply, reply_id=reply_id)
    comment_id = reply.comment.comment_id
    
    if request.method == 'POST':
        reply_text = request.POST.get('reply_text')
        reply.reply_text = reply_text
        reply.save()
        return redirect('comment_detail', comment_id=comment_id)
    
    context = {'reply': reply}
    return render(request, 'reply/edit_reply.html', context)

def delete_reply(request, reply_id):
    reply = get_object_or_404(Reply, reply_id=reply_id)
    comment_id = reply.comment.comment_id
    
    if request.method == 'POST':
        reply.delete()
        return redirect('comment_detail', comment_id=comment_id)
    
    context = {'reply': reply}
    return render(request, 'reply/delete_reply.html', context)
