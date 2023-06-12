from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField(User, related_name="friends")
    followers = models.ManyToManyField(User, related_name="followers")
    following = models.ManyToManyField(User, related_name="following")
    archived_posts = models.ManyToManyField('posts.Post',related_name="archived_posts")
    profile_picture = models.ImageField(upload_to="profile_pictures")
    bio = models.TextField()


    def __str__(self) -> str:
        return  self.user.username
