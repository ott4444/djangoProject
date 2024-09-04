# moviesearch/views.py
import requests
from django.shortcuts import render
from django.conf import settings
from .models import Search, SearchMovie

TMDB_SEARCH_URL = 'https://api.themoviedb.org/3/search/movie'

def sample_view(request):
    # Simple view for testing
    return render(request, 'sample.html')

def search_movies(request):
    searchInput = request.GET.get('searchInput', '').strip().lower()
    if not searchInput:
        # Handle the case where no search input is provided
        return render(request, 'moviesearch/search_results.html', {'results': []})
        # Check if the search query exists in the database
    search, created = Search.objects.get_or_create(query=searchInput)
    print(f"Search Query: '{searchInput}', Created: {created}")
    if not created:
        # If search query exists, return the cached results
        movies = SearchMovie.objects.filter(search=search)
    else:
        # If search query does not exist, fetch from TMDB
        url = f'{TMDB_SEARCH_URL}?api_key={settings.TMDB_API_KEY}&searchInput={searchInput}'
        response = requests.get(url)
        tmdb_movies = response.json().get('results', [])
        # Save the movies returned by TMDB
        movies = []
        for tmdb_movie in tmdb_movies:
            movie, created = SearchMovie.objects.get_or_create(
                search=search,
                tmdb_id=tmdb_movie['id'],
                defaults={
                    'title': tmdb_movie['title'],
                    'release_date': tmdb_movie.get('release_date'),
                    'overview': tmdb_movie.get('overview'),
                    'poster_path': tmdb_movie.get('poster_path'),
                }
            )
            movies.append(movie)
            print(f"Number of movies saved for '{searchInput}': {len(movies)}")
    return render(request, 'moviesearch/search_results.html', {'results': movies})

def movie_detail(request, movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={settings.TMDB_API_KEY}&language=en-US'
    response = requests.get(url)
    if response.status_code == 200:
        movie = response.json()
    else:
        movie = {}
    return render(request, 'moviesearch/movie_detail.html', {'movie': movie})

