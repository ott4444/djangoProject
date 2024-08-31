# userprofiles/forms.py

from django import forms
from .models import Profile  # Adjust the import according to your model

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'bio']  # List the fields you want in the form
