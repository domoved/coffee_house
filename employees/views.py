from django.shortcuts import render, redirect
from coffee_house.forms import UserRegistrationForm
from .models import UserProfile
from courses.models import Lecture, Test, Course
from django.contrib.auth.forms import UserCreationForm


def employee_list(request):
    employees = UserProfile.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})


def intern_dashboard(request):
    courses = Course.objects.filter(role='intern')
    lectures = Lecture.objects.all()
    tests = Test.objects.all()
    return render(request, 'roles/intern_dashboard.html',
                  {'courses': courses, 'lectures': lectures, 'tests': tests})
