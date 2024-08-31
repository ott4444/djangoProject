# watchlists/models.py
from django.db import models
from django.contrib.auth.models import User
from djangoProject import settings
from moviesearch.models import Movie


class Watchlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    movies = models.ManyToManyField(Movie, blank=True)

    def __str__(self):
        return self.name

