from django.urls import path
from .views import sample_view
from .views import search_movies, movie_detail

urlpatterns = [
    path('sample/', sample_view, name='sample'),
    path('search/', search_movies, name='search_movies'),
    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),
]



