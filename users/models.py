from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=255)

    def full_name(self):
        """Returns the full name of the user."""
        return f"{self.first_name} {self.last_name}"

    def set_password(self, new_password):
        """Sets a new password for the user."""
        self.password = new_password
        self.save()

    def get_user_by_email(email):
        """Retrieves a user instance based on the given email."""
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

    def __str__(self):
        """Returns a string representation of the user."""
        return self.username
