from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserRegistrationForm
from employees.models import UserProfile


def get_dashboard_redirect_url(role):
    role_map = {
        'intern': 'intern_dashboard',
        'barista': 'barista_dashboard',
        'manager': 'manager_dashboard',
        'supervisor': 'supervisor_dashboard',
        'hr_manager': 'hr_manager_dashboard',
    }
    return role_map.get(role, 'home')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                user_profile = UserProfile.objects.get(user=user)
                role = user_profile.role
                return redirect(get_dashboard_redirect_url(role))
            except UserProfile.DoesNotExist:
                messages.error(request, 'Профиль пользователя не найден')
                return redirect('home')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль')
            return redirect('login')
    else:
        return render(request, 'login.html')


def home(request):
    return render(request, 'base.html')
