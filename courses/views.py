from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from courses.models import Lecture, Test, Course
from employees.models import UserProfile


def get_available_courses(user_profile):
    courses = Course.objects.all()
    available_courses = []
    for course in courses:
        if user_profile and user_profile.role in course.role_hierarchy():
            available_courses.append(course)
    return available_courses


@login_required
def intern_dashboard(request):
    try:
        user_profile = getattr(request.user, 'userprofile', None)
        available_courses = get_available_courses(user_profile)
        lectures = Lecture.objects.all()
        tests = Test.objects.all()
        return render(request, 'courses/intern_dashboard.html',
                      {'courses': available_courses, 'lectures': lectures, 'tests': tests})
    except UserProfile.DoesNotExist:
        return HttpResponse("Профиль стажера не найден")


@login_required
def hr_manager_dashboard(request):
    try:
        user_profile = getattr(request.user, 'userprofile', None)
        available_courses = get_available_courses(user_profile)
        lectures = Lecture.objects.all()
        tests = Test.objects.all()
        return render(request, 'courses/hr_manager_dashboard.html',
                      {'courses': available_courses, 'lectures': lectures, 'tests': tests})
    except UserProfile.DoesNotExist:
        return HttpResponse("Профиль менеджера по персоналу не найден")


@login_required
def course_list(request):
    user_profile = getattr(request.user, 'userprofile', None)
    available_courses = get_available_courses(user_profile)
    return render(request, 'courses/courses.html',
                  {'courses': available_courses, 'user_profile': user_profile})


@login_required
def course_detail(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    return render(request, 'course_detail.html', {'course': course})
