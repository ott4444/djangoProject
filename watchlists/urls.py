# watchlists/urls.py
from django.urls import path
from .views import create_watchlist, add_movie_to_watchlist

urlpatterns = [
    path('create/', create_watchlist, name='create_watchlist'),
    path('add/<int:watchlist_id>/<int:movie_id>/', add_movie_to_watchlist, name='add_movie_to_watchlist'),
]
