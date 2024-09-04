
from django.db import models

class Search(models.Model):
    query = models.CharField(max_length=255, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query

class SearchMovie(models.Model):
    search = models.ForeignKey(Search, related_name='movies', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    tmdb_id = models.IntegerField(unique=True)
    release_date = models.DateField(null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    poster_path = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True)  # TMDB ID for the movie
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=255)
    overview = models.TextField()
    poster_path = models.CharField(max_length=255, blank=True, null=True)  # Path to the poster image


    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.title
