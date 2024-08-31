from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required

@login_required

def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile_detail', profile_id=request.user.profile.id)
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'userprofiles/edit_profile.html', {'form': form})

def profile_detail(request, profile_id):  # Renamed the parameter to avoid shadowing 'id'
    profile = get_object_or_404(Profile, id=profile_id)
    return render(request, 'userprofiles/profile_detail.html', {'profile': profile})

def profile_view(request):
    # Retrieve the current user's profile. Adjust as necessary.
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'userprofiles/profile_detail.html', {'profile': profile})
