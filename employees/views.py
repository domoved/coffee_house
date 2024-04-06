from django.shortcuts import render, redirect
from courses.models import Lecture, Test, Course
from employees.models import UserProfile, Role


def employee_list(request):
    employees = UserProfile.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})


def intern_dashboard(request):
    intern_role = Role.objects.get(role='intern')
    courses = Course.objects.filter(role=intern_role)
    lectures = Lecture.objects.all()
    tests = Test.objects.all()
    return render(request, 'roles/intern_dashboard.html',
                  {'courses': courses, 'lectures': lectures, 'tests': tests})
