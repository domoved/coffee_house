from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = (
        ('intern', 'Стажер'),
        ('barista', 'Бариста'),
        ('manager', 'Менеджер'),
        ('supervisor', 'Управляющий'),
        ('hr_manager', 'Менеджер по персоналу'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.user.username}"
