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

