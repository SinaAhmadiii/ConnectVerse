from django.shortcuts import render, get_object_or_404, redirect
from users.models import User
from post.models import Post
from .models import Bookmark

def bookmark_post(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    
    if request.method == 'POST':
        bookmark = Bookmark(user=request.user, post=post)
        bookmark.save()
        return redirect('post_detail', post_id=post_id)
    
    context = {'post': post}
    return render(request, 'bookmark/bookmark_post.html', context)

def remove_bookmark(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, bookmark_id=bookmark_id)
    post_id = bookmark.post.post_id
    
    if request.method == 'POST':
        bookmark.delete()
        return redirect('post_detail', post_id=post_id)
    
    context = {'bookmark': bookmark}
    return render(request, 'bookmark/remove_bookmark.html', context)

def user_bookmarks(request, username):
    user = get_object_or_404(User, username=username)
    bookmarks = Bookmark.objects.filter(user=user)
    
    context = {'user': user, 'bookmarks': bookmarks}
    return render(request, 'bookmark/user_bookmarks.html', context)
