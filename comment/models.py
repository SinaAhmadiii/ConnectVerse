from django.db import models
from users.models import User
from post.models import Post
from django.conf import settings


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True, verbose_name='Comment ID')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')
    comment_text = models.TextField(verbose_name='Comment Text', help_text='Enter your comment here.')

    def __str__(self):
        return f"Comment {self.comment_id} by {self.user.username} on Post {self.post.post_id}"

    def get_comment_id(self):
        return self.comment_id

    def get_user(self):
        return self.user

    def get_post(self):
        return self.post

    def get_comment_text(self):
        return self.comment_text
