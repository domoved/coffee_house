from django.shortcuts import render
from .models import UserProfile, Role
from courses.models import Lecture, Test, Course


def employee_list(request):
    employees = UserProfile.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})


def intern_dashboard(request):
    courses = Course.objects.filter(role='intern')
    lectures = Lecture.objects.all()
    tests = Test.objects.all()
    return render(request, 'roles/intern_dashboard.html',
                  {'courses': courses, 'lectures': lectures, 'tests': tests})
