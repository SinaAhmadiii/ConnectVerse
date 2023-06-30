from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(
        max_length=255,
        verbose_name='First Name',
        help_text='The user\'s first name.'
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name='Last Name',
        help_text='The user\'s last name.'
    )
    username = models.CharField(
        unique=True,
        max_length=255,
        verbose_name='Username',
        help_text='The unique username for the user.'
    )
    email = models.EmailField(
        unique=True,
        verbose_name='Email',
        help_text='The unique email address for the user.'
    )
    age = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Age',
        help_text='The age of the user (optional).'
    )
    phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name='Phone Number',
        help_text='The phone number of the user (optional).'
    )

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.username

    def get_age(self):
        return self.age

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
        self.save()

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email
        self.save()
