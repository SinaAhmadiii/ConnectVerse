from django import forms
from users.models import User
from post.models import Post
from .models import Bookmark

class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ['user', 'post']

    def get_user_bookmarks(self, user):
        return Bookmark.objects.filter(user=user)

    def get_bookmarked_posts(self, user):
        return Post.objects.filter(bookmark__user=user)

    def bookmark_post(self, user, post):
        bookmark = Bookmark(user=user, post=post)
        bookmark.save()
