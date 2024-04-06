from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from courses.models import Lecture, Test, Course
from employees.models import UserProfile


def employee_list(request):
    employees = UserProfile.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})


@login_required
def intern_dashboard(request):
    try:
        intern_roles = UserProfile.objects.filter(role='intern')
        courses = Course.objects.filter(role__in=intern_roles)
        lectures = Lecture.objects.all()
        tests = Test.objects.all()
        return render(request, 'courses/intern_dashboard.html',
                      {'courses': courses, 'lectures': lectures, 'tests': tests})
    except UserProfile.DoesNotExist:
        return HttpResponse("Профиль стажера не найден")
