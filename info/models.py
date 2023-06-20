from django.db import models
from users.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures')
    account_created = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Profile for {self.user.username}"
