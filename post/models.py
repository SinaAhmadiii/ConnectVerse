from django.db import models
from users.models import User
from django.conf import settings


class Post(models.Model):
    post_id = models.AutoField(primary_key=True, verbose_name='Post ID')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    post_text = models.TextField(verbose_name='Post Text', help_text='Enter the text for the post.')
    likes_count = models.IntegerField(default=0, verbose_name='Likes Count')
    views_count = models.IntegerField(default=0, verbose_name='Views Count')

    def __str__(self):
        return f"Post {self.post_id} by {self.user.username}"

    def increment_likes(self):
        self.likes_count += 1
        self.save()
