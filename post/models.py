from django.db import models
from users.models import User

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_text = models.TextField()
    likes_count = models.IntegerField(default=0)
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Post {self.post_id} by {self.user.username}"
