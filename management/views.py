from django.shortcuts import render, get_object_or_404

from employees.models import UserProfile


def role_list(request):
    roles = UserProfile.objects.all()
    return render(request, 'management/role_list.html', {'roles': roles})


def role_detail(request, role_id):
    role = get_object_or_404(UserProfile.role, pk=role_id)
    return render(request, 'management/role_detail.html', {'role': role})
