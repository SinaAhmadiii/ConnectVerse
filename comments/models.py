from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.content