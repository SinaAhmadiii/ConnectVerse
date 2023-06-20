from django.db import models
from users.models import User
from post.models import Post

class Bookmark(models.Model):
    bookmark_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"Bookmark ID: {self.bookmark_id}"
