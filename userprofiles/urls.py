# userprofiles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view, name='profile'),  # Maps to profile_view function
    path('edit/', views.edit_profile, name='edit_profile'),
    path('profile/<int:profile_id>/', views.profile_detail, name='profile_detail'),  # Updated the parameter name
]
