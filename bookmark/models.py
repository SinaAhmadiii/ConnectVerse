from django.db import models
from users.models import User
from post.models import Post
from django.conf import settings


class Bookmark(models.Model):
    bookmark_id = models.AutoField(primary_key=True, verbose_name='Bookmark ID')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', help_text='The user who bookmarked the post')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post', help_text='The post that was bookmarked')

    def __str__(self):
        return f"Bookmark ID: {self.bookmark_id}"

    def get_user_bookmarks(self, user):
        return Bookmark.objects.filter(user=user)

    def get_bookmarked_posts(self, user):
        return Post.objects.filter(bookmark__user=user)

    def bookmark_post(self, user, post):
        bookmark = Bookmark(user=user, post=post)
        bookmark.save()
