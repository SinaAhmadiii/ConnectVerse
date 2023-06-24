from django.db import models
from users.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User")
    profile_picture = models.ImageField(upload_to='profile_pictures', verbose_name="Profile Picture", help_text="Upload a profile picture.")
    account_created = models.DateTimeField(auto_now_add=True, verbose_name="Account Created", help_text="The date and time when the account was created.")
    bio = models.TextField(blank=True, verbose_name="Bio", help_text="Enter a short bio about yourself.")

    def __str__(self):
        return f"Profile for {self.user.username}"

    def get_full_name(self):
        return self.user.get_full_name()

    def get_username(self):
        return self.user.username

    def update_profile_picture(self, new_picture):
        self.profile_picture = new_picture
        self.save()

    def add_bio(self, new_bio):
        self.bio = new_bio
        self.save()

    def delete_profile(self):
        self.user.delete()
        self.delete()
