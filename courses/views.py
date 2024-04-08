from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from coffee_house.forms import TestForm, QuestionForm
from courses.models import Lecture, Test, Course
from employees.models import UserProfile
from .models import Answer


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


@login_required
def create_or_update_test(request, course_slug):
    course = Course.objects.get(slug=course_slug)

    if request.method == 'POST':
        test_form = TestForm(request.POST)
        if test_form.is_valid():
            test = test_form.save(commit=False)
            test.course = course
            test.save()
            for key, value in request.POST.items():
                if key.startswith('question_text'):
                    question_form = QuestionForm({'question_text': value})
                    if question_form.is_valid():
                        question = question_form.save(commit=False)
                        question.test = test
                        question.save()
                        answer_keys = [k for k in request.POST.keys() if
                                       k.startswith(f'answer_text_{key.split("_")[2]}')]
                        for answer_key in answer_keys:
                            answer_text = request.POST.get(answer_key, '')
                            is_correct_key = answer_key.replace('answer_text', 'is_correct')
                            is_correct_values = request.POST.getlist(is_correct_key)
                            is_correct = "True" in is_correct_values
                            answer = Answer(answer_text=answer_text, is_correct=is_correct, question=question)
                            answer.save()

            return redirect('course_detail', course_slug=course_slug)
    else:
        test_form = TestForm()
    return render(request, 'courses/create_or_update_test.html', {'test_form': test_form})
