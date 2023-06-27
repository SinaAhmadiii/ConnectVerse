from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def create_post(request):
    if request.method == 'POST':
        post_text = request.POST.get('post_text')
        post = Post(user=request.user, post_text=post_text)
        post.save()
        return redirect('home')
    
    return render(request, 'post/create_post.html')

def edit_post(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    
    if request.method == 'POST':
        post_text = request.POST.get('post_text')
        post.post_text = post_text
        post.save()
        return redirect('home')
    
    context = {'post': post}
    return render(request, 'post/edit_post.html', context)

def delete_post(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    
    context = {'post': post}
    return render(request, 'post/delete_post.html', context)
