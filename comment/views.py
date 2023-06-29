from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Comment
from .forms import CommentForm

class CommentListView(ListView):
    model = Comment
    template_name = 'comment/comment_list.html'  
    context_object_name = 'comments'  

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment/comment_create.html'  
    success_url = reverse_lazy('comment_list')  

class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment/comment_update.html'  
    success_url = reverse_lazy('comment_list')  

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comment/comment_delete.html'  
    success_url = reverse_lazy('comment_list')  