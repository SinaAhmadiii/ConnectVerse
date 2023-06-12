from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    category_tags = models.ManyToManyField("categories.Category")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(User, related_name="liked_posts")
    disliked_by = models.ManyToManyField(User, related_name="disliked_posts")


    def __str__(self):
        return self.title
    