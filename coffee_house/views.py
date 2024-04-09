from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from coffee_house import roles
from courses.models import Course, LearningProgress, Test, Question
from employees.models import UserProfile
from .forms import UserRegistrationForm, LectureForm, CourseForm, QuestionForm, TestForm, AnswerForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            UserProfile.objects.create(user=user, role='intern')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not UserProfile.objects.filter(user__username=username).exists():
            messages.error(request, 'Пользователь с таким именем не найден')
            return render(request, 'login.html')

        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Неправильный пароль')
            return render(request, 'login.html')
        login(request, user)

        try:
            user_profile = UserProfile.objects.get(user=user)
            role = user_profile.role
            return redirect('dashboard')
        except UserProfile.DoesNotExist:
            messages.error(request, 'Профиль пользователя не найден')

    return render(request, 'login.html')


@login_required
def profile(request):
    user_profile = request.user.userprofile
    available_courses = Course.objects.filter(role__in=roles.ROLE_HIERARCHY_ACCESS[user_profile.role])
    progress = LearningProgress.objects.filter(user=user_profile)
    lecture_form = LectureForm()
    test_form = TestForm()
    course_form = CourseForm()
    question_form = QuestionForm()
    context = {'user_profile': user_profile, 'available_courses': available_courses, 'progress': progress}

    if user_profile.role in ['manager', 'supervisor', 'hr_manager']:
        intern_progress = LearningProgress.objects.filter(user__role='intern', course__role='intern')
        barista_progress = LearningProgress.objects.filter(user__role='barista', course__role='barista')
        context['barista_progress'] = barista_progress
        context['intern_progress'] = intern_progress

    if user_profile.role in ['supervisor', 'hr_manager']:
        manager_progress = LearningProgress.objects.filter(user__role='manager', course__role='manager')
        context['manager_progress'] = manager_progress

    if user_profile.role == 'hr_manager':
        context['available_courses'] = Course.objects.all()
        supervisor_progress = LearningProgress.objects.filter(user__role='supervisor', course__role='supervisor')
        context['supervisor_progress'] = supervisor_progress

        if request.method == 'POST':
            if 'add_course' in request.POST:
                course_form = CourseForm(request.POST)
                if course_form.is_valid():
                    title = course_form.cleaned_data['title']
                    description = course_form.cleaned_data['description']
                    role = course_form.cleaned_data['role']
                    video_url = course_form.cleaned_data['video_url']
                    course = Course(title=title, description=description, role=role,
                                    video_url=video_url)
                    course.save()
                    return redirect('profile')
            elif 'add_lecture' in request.POST:
                lecture_form = LectureForm(request.POST)
                if lecture_form.is_valid():
                    course_slug = request.POST.get('course_slug')
                    course = get_object_or_404(Course, course_slug=course_slug)
                    lecture = lecture_form.save(commit=False)
                    lecture.course = course
                    lecture.save()
                    return redirect('profile')
            elif 'add_test' in request.POST:
                test_form = TestForm(request.POST)
                if test_form.is_valid():
                    course_slug = request.POST.get('course_slug')
                    course = get_object_or_404(Course, course_slug=course_slug)
                    test = test_form.save(commit=False)
                    test.course = course
                    test.save()
                    return redirect('profile')
            elif 'add_question' in request.POST:
                question_form = QuestionForm(request.POST)
                if question_form.is_valid():
                    question = question_form.save(commit=False)
                    question.test = Test.objects.get(test_slug=request.POST.get('test_slug'))
                    question.save()
                    return redirect('profile')
            elif 'add_answer' in request.POST:
                answer_form = AnswerForm(request.POST)
                if answer_form.is_valid():
                    answer = answer_form.save(commit=False)
                    answer.question = Question.objects.get(pk=request.POST.get('question_id'))
                    answer.save()
                    return redirect('profile')

        context = {'user_profile': user_profile,
                   'available_courses': available_courses,
                   'progress': progress,
                   'lecture_form': lecture_form,
                   'test_form': test_form,
                   'course_form': course_form,
                   'question_form': question_form}

    return render(request, 'profile.html', context)


def upgrade_role(request, username):
    user = get_object_or_404(UserProfile, user__username=username)
    user.upgrade_role()
    return redirect('profile')


def home(request):
    return render(request, 'base.html')
