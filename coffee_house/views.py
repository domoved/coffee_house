from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from employees.models import UserProfile
from .forms import UserRegistrationForm

role_dashboard_mapping = {
    'intern': 'intern_dashboard',
    'barista': 'barista_dashboard',
    'manager': 'manager_dashboard',
    'supervisor': 'supervisor_dashboard',
    'hr_manager': 'hr_manager_dashboard',
}


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            UserProfile.objects.create(user=user, role='intern')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not UserProfile.objects.filter(user__username=username).exists():
            messages.error(request, 'Пользователь с таким именем не найден')
            return render(request, 'login.html')

        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Неправильный пароль')
            return render(request, 'login.html')
        login(request, user)

        try:
            user_profile = UserProfile.objects.get(user=user)
            role = user_profile.role
            dashboard_url = role_dashboard_mapping.get(role)
            if dashboard_url:
                return redirect(dashboard_url)
            else:
                messages.error(request, 'Неправильная роль пользователя')
        except UserProfile.DoesNotExist:
            messages.error(request, 'Профиль пользователя не найден')

    return render(request, 'login.html')


def home(request):
    return render(request, 'base.html')
