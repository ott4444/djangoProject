# moviedetails/views.py
import requests
from django.shortcuts import render
from django.http import HttpResponse

TMDB_MOVIE_URL = 'https://api.themoviedb.org/3/movie/'


def movie_detail(request, movie_id):
    api_key = '71c28d0bbc034d9385032100b32e03db'  # Replace with your actual API key
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        movie = response.json()
        return render(request, 'moviedetails/movie_detail.html', {'movie': movie})
    else:
        error_message = response.json().get('status_message', 'Unknown error')
        return render(request, 'moviedetails/movie_detail.html', {
            'error': error_message,
        })
def home(request):
    return HttpResponse("Welcome to the Home Page!")
