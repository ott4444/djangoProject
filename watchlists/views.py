# watchlists/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Watchlist
from moviesearch.models import Movie

def create_watchlist(request):
    # Implement create view
    pass

def add_movie_to_watchlist(request, watchlist_id, movie_id):
    watchlist = get_object_or_404(Watchlist, id=watchlist_id)
    movie = get_object_or_404(Movie, id=movie_id)
    watchlist.movies.add(movie)
    return redirect('watchlist_detail', watchlist_id=watchlist.id)
