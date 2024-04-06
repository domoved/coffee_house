from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Course


@login_required
def course_list(request):
    user_profile = request.user.userprofile
    courses = Course.objects.all()
    available_courses = []
    for course in courses:
        if user_profile.role in course.role_hierarchy():
            available_courses.append(course)
    return render(request, 'courses/courses.html',
                  {'courses': available_courses, 'user_profile': user_profile})

