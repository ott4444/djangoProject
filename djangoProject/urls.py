from django.contrib import admin
from django.urls import path, include
from moviedetails import urls as moviedetails_urls



urlpatterns = [
    path('admin/', admin.site.urls), # Redirect root URL to admin page
    path('profile/', include('userprofiles.urls')),
    path('moviesearch/', include('moviesearch.urls')),
    path('moviedetails/', include(moviedetails_urls)),
    path('watchlists/', include('watchlists.urls')),
    path('accounts/', include('accounts.urls')),
]
