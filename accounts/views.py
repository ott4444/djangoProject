# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Account
from django.contrib.auth import get_user_model


@login_required

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/register.html'

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


def account_detail(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    return render(request, 'accounts/account_detail.html', {'account': account})


def account_view(request):
    user = get_user_model()
    user = user.objects.get(pk=1)
    account = get_object_or_404(user, id=request.user.id)
    return render(request, 'accounts/account_detail.html', {'account': account})