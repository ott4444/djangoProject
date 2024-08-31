# userprofiles/models.py

from django.db import models
from django.contrib.auth.models import User
from djangoProject import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # Ensure these fields are defined
    email = models.EmailField()  # Email field
    bio = models.TextField(blank=True)  # Bio field

    def __str__(self):
        return self.user


