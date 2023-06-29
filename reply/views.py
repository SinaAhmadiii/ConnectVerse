from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Reply
from .forms import ReplyForm

class ReplyCreateView(CreateView):
    model = Reply
    form_class = ReplyForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.comment_id = self.kwargs['comment_id']
        return super().form_valid(form)

class ReplyUpdateView(UpdateView):
    model = Reply
    form_class = ReplyForm
    template_name_suffix = '_update'

class ReplyDeleteView(DeleteView):
    model = Reply
    success_url = reverse_lazy('comment-list')  
    template_name_suffix = '_confirm_delete'
