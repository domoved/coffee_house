from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from coffee_house.roles import ROLE_CHOICES
from courses.models import Test, Question, Answer, Lecture, Course
from employees.models import Document


class DocumentForm(forms.ModelForm):
    document = forms.FileField(label='Выберите файл')
    title = forms.CharField(label='Название документа', max_length=100)

    class Meta:
        model = Document
        fields = ['title', 'document']
        labels = {'title': 'Название документа', 'document': 'Выберите файл'}


class LectureForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    course_slug = forms.CharField()

    class Meta:
        model = Lecture
        fields = ['title', 'content', 'course_slug']


class CourseForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    role = forms.ChoiceField(choices=ROLE_CHOICES)
    video_url = forms.URLField()

    class Meta:
        model = Course
        fields = ['title', 'description', 'role', 'video_url']
        labels = {'title': 'Название', 'description': 'Описание', 'video_url': 'URL видео'}


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        labels = {'question_text': 'Текст вопроса'}


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text', 'is_correct']
        labels = {'answer_text': 'Текст ответа', 'is_correct': 'Правильный ответ'}


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['title']
        labels = {'title': 'Название теста'}


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               widget=forms.TextInput(attrs={'placeholder': 'Введите имя', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Введите email', 'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', 'class': 'form-control'}))
    password_check = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_username(self):
        username = self.cleaned_data['username']

        if User.objects.filter(username=username).exists():
            raise ValidationError("Пользователь с таким именем уже существует.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise ValidationError("Пользователь с таким email уже существует.")
        return email

    def clean(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get('password')
        password_check = cleaned_data.get('password_check')

        if password != password_check:
            raise ValidationError('password_check', 'Пароли не совпадают.')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
