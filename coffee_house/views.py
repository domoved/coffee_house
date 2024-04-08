from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from courses.models import Course, LearningProgress, Test, Lecture
from employees.models import UserProfile
from .forms import UserRegistrationForm


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
            return redirect('dashboard')
        except UserProfile.DoesNotExist:
            messages.error(request, 'Профиль пользователя не найден')

    return render(request, 'login.html')


@login_required
def profile(request):
    user_profile = request.user.userprofile

    intern_progress = LearningProgress.objects.filter(user__role='intern')
    barista_progress = LearningProgress.objects.filter(user__role='barista')
    manager_progress = LearningProgress.objects.filter(user__role='manager')
    supervisor_progress = LearningProgress.objects.filter(user__role='supervisor')
    available_courses = Course.objects.filter(role=user_profile.role)
    progress = LearningProgress.objects.filter(user=user_profile)
    context = {'user_profile': user_profile, 'available_courses': available_courses, 'progress': progress}

    if user_profile.role == 'manager':
        context['intern_progress'] = user_profile.role_hierarchy(user_profile.role)
        context['barista_progress'] = barista_progress

    if user_profile.role == 'supervisor':
        context['intern_progress'] = intern_progress
        context['barista_progress'] = barista_progress
        context['manager_progress'] = manager_progress

    if user_profile.role == 'hr_manager':
        other_users = UserProfile.objects.exclude(user=request.user)
        courses = Course.objects.all()
        tests = Test.objects.all()
        lectures = Lecture.objects.all()
        context.update({'other_users': other_users, 'courses': courses, 'tests': tests, 'lectures': lectures})

    return render(request, 'profile.html', context)


def home(request):
    return render(request, 'base.html')
