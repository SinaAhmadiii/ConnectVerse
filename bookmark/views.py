from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Bookmark
from .forms import BookmarkForm

class BookmarkListView(ListView):
    model = Bookmark
    template_name = 'bookmark_list.html'
    context_object_name = 'bookmarks'

    def get_queryset(self):
        user = self.request.user
        return Bookmark.objects.filter(user=user)

class BookmarkCreateView(CreateView):
    model = Bookmark
    form_class = BookmarkForm
    template_name = 'bookmark_create.html'
    success_url = reverse_lazy('bookmark_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
