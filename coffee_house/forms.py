from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password_check = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_check']:
            raise forms.ValidationError('Пароли не совпадают!')
        return cd['password_check']


