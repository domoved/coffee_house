from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from coffee_house.forms import TestForm, QuestionForm
from courses.models import Lecture, Test, Course, LearningProgress, Grade
from employees.models import UserProfile
from .models import Answer


def get_available_courses(user_profile):
    courses = Course.objects.all()
    available_courses = []
    for course in courses:
        if user_profile and user_profile.role in course.role_hierarchy:
            available_courses.append(course)
    return available_courses


@login_required
def create_or_update_test(request, course_slug):
    course = Course.objects.get(course_slug=course_slug)

    if request.method == 'POST':
        test_form = TestForm(request.POST)
        if test_form.is_valid():
            test = test_form.save(commit=False)
            test.course = course
            test.save()
            save_questions_and_answers(request, test)
            return redirect('course_detail', course_slug=course_slug)
    else:
        test_form = TestForm()
    return render(request, 'courses/create_or_update_test.html', {'test_form': test_form})


def save_questions_and_answers(request, test):
    for key, value in request.POST.items():
        if key.startswith('question_text'):
            question_form = QuestionForm({'question_text': value})
            if question_form.is_valid():
                question = question_form.save(commit=False)
                question.test = test
                question.save()
                save_answers(request, key, question)


def save_answers(request, question_key, question):
    answer_keys = [k for k in request.POST.keys() if k.startswith(f'answer_text_{question_key.split("_")[2]}')]
    for answer_key in answer_keys:
        answer_text = request.POST.get(answer_key, '')
        is_correct_key = answer_key.replace('answer_text', 'is_correct')
        is_correct_values = request.POST.getlist(is_correct_key)
        is_correct = "on" in is_correct_values
        answer = Answer(answer_text=answer_text, is_correct=is_correct, question=question)
        answer.save()


@login_required
def dashboard(request):
    try:
        user_profile = getattr(request.user, 'userprofile', None)
        available_courses = get_available_courses(user_profile)
        lectures = Lecture.objects.all()
        tests = Test.objects.all()
        role = user_profile.role if user_profile else None
        return render(request, 'courses/dashboard.html',
                      {'role': role, 'courses': available_courses, 'lectures': lectures, 'tests': tests})
    except UserProfile.DoesNotExist:
        return HttpResponse("Профиль пользователя не найден")


@login_required
def course_list(request):
    user_profile = getattr(request.user, 'userprofile', None)
    available_courses = get_available_courses(user_profile)
    return render(request, 'courses/courses.html',
                  {'courses': available_courses, 'user_profile': user_profile})


@login_required
def course_detail(request, course_slug):
    course = get_object_or_404(Course, course_slug=course_slug)
    return render(request, 'course_detail.html', {'course': course})


@login_required
def test_detail(request, course_slug, test_slug):
    test = get_object_or_404(Test, test_slug=test_slug)
    questions = test.question_set.all()
    answers_map = {answer.id: answer.is_correct for question in questions for answer in question.answer_set.all()}
    return render(request, 'test_detail.html', {'test': test, 'answers_map': answers_map})


def submit_test(request, course_slug, test_slug):
    test = get_object_or_404(Test, course__course_slug=course_slug, test_slug=test_slug)
    if request.method == 'POST':
        user_answers = {int(key.replace('question', '')): int(value) for key, value in request.POST.items() if
                        key.startswith('question')}
        results = {}
        correct_answers = 0
        for question in test.question_set.all():
            correct_answer_id = question.answer_set.filter(is_correct=True).first().id
            user_answer_id = user_answers.get(question.id)
            results[question] = correct_answer_id == user_answer_id
            if results[question]:
                correct_answers += 1

        grade = correct_answers * 100 / len(user_answers) if user_answers else 0
        user_profile = request.user.userprofile
        Grade.objects.update_or_create(
            user=user_profile,
            test=test,
            defaults={'grade': grade}
        )
        try:
            progress = LearningProgress.objects.get(user=user_profile, course=test.course)
        except ObjectDoesNotExist:
            progress = LearningProgress.objects.create(user=user_profile, course=test.course)
        else:
            progress.calculate_completion_percentage()
            progress.save()

    return render(request, 'test_detail.html',
                  {'test': test, 'results': results, 'answers': len(user_answers), 'correct_answers': correct_answers})


@login_required
def lecture_detail(request, course_slug, lecture_slug):
    lecture = get_object_or_404(Lecture, lecture_slug=lecture_slug)
    return render(request, 'lecture_detail.html', {'lecture': lecture})




