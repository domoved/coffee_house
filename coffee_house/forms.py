from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password_check = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        password_check = cleaned_data.get('password_check')

        if not username:
            self.add_error('username', 'Пожалуйста, введите имя пользователя.')
        if not email:
            self.add_error('email', 'Пожалуйста, введите адрес электронной почты.')
        if not password:
            self.add_error('password', 'Пожалуйста, введите пароль.')
        if not password_check:
            self.add_error('password_check', 'Пожалуйста, введите пароль повторно.')

        if password and password_check and password != password_check:
            self.add_error('password', 'Пароли не совпадают.')
            self.add_error('password_check', 'Пароли не совпадают.')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
