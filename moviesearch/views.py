# moviesearch/views.py
import requests
from django.shortcuts import render
from django.conf import settings  # Import settings

TMDB_SEARCH_URL = 'https://api.themoviedb.org/3/search/movie'

def sample_view(request):
    # Simple view for testing
    return render(request, 'sample.html')

def search_movies(request):
    query = request.GET.get('query')
    if query:
        url = f'{TMDB_SEARCH_URL}?api_key={settings.TMDB_API_KEY}&query={query}'
        response = requests.get(url)
        results = response.json().get('results', [])
    else:
        results = []
    return render(request, 'moviesearch/search_results.html', {'results': results})

def movie_detail(request, movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={settings.TMDB_API_KEY}&language=en-US'
    response = requests.get(url)
    if response.status_code == 200:
        movie = response.json()
    else:
        movie = {}
    return render(request, 'moviesearch/movie_detail.html', {'movie': movie})
