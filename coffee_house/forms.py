from django import forms
from django.contrib.auth.models import User
from django.forms import inlineformset_factory

from courses.models import Test, Question, Answer


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text', 'is_correct']
        widgets = {
            'answer_text': forms.TextInput(attrs={'class': 'form-control'}),
            'is_correct': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }


AnswerFormSet = inlineformset_factory(Question, Answer, form=AnswerForm, extra=1, can_delete=False)


class TestForm(forms.ModelForm):
    questions = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    answers = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Test
        fields = ['title', 'course', 'questions', 'answers']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'course': forms.Select(attrs={'class': 'form-control'})}


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

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        password_check = cleaned_data.get('password_check')

        if password != password_check:
            self.add_error('password_check', 'Пароли не совпадают.')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
