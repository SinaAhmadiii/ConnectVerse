from django.shortcuts import render, get_object_or_404, redirect
from post.models import Post
from .models import Comment

def create_comment(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    
    if request.method == 'POST':
        comment_text = request.POST.get('comment_text')
        comment = Comment(user=request.user, post=post, comment_text=comment_text)
        comment.save()
        return redirect('post_detail', post_id=post_id)
    
    context = {'post': post}
    return render(request, 'comment/create_comment.html', context)

def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, comment_id=comment_id)
    post_id = comment.post.post_id
    
    if request.method == 'POST':
        comment_text = request.POST.get('comment_text')
        comment.comment_text = comment_text
        comment.save()
        return redirect('post_detail', post_id=post_id)
    
    context = {'comment': comment}
    return render(request, 'comment/edit_comment.html', context)

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, comment_id=comment_id)
    post_id = comment.post.post_id
    
    if request.method == 'POST':
        comment.delete()
        return redirect('post_detail', post_id=post_id)
    
    context = {'comment': comment}
    return render(request, 'comment/delete_comment.html', context)
