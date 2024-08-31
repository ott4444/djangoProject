from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# Custom User Creation Form
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()  # Use the custom user model if specified
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

# User Profile Form
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()  # Correctly reference the user model class
        fields = ['username', 'email']  # Adjust fields as necessary
