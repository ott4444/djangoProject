
from django.db import models

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
