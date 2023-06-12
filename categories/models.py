from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=300)
    followers = models.ManyToManyField(User, related_name="followed_categories")


    def __str__(self):
        return self.name