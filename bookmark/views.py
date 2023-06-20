from django.shortcuts import render, get_object_or_404
from .models import Bookmark
from post.models import Post

def bookmark_list(request):
    bookmarks = Bookmark.objects.filter(user=request.user)
    return render(request, 'bookmark_list.html', {'bookmarks': bookmarks})

def bookmark_detail(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, bookmark_id=bookmark_id, user=request.user)
    return render(request, 'bookmark_detail.html', {'bookmark': bookmark})

def bookmark_post(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    bookmark, created = Bookmark.objects.get_or_create(user=request.user, post=post)
    if created:
        message = 'Post bookmarked successfully!'
    else:
        message = 'Post already bookmarked!'
    return render(request, 'bookmark_post.html', {'message': message})

def remove_bookmark(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, bookmark_id=bookmark_id, user=request.user)
    bookmark.delete()
    return render(request, 'remove_bookmark.html')
