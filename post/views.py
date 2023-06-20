from django.shortcuts import render
from .models import Post

def post_detail(request, post_id):
    post = Post.objects.get(post_id=post_id)
    return render(request, 'post_detail.html', {'post': post})
