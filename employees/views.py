from django.shortcuts import render
from .models import UserProfile


def employee_list(request):
    employees = UserProfile.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})
