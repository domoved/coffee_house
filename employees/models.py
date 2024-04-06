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


class Review(models.Model):
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=5)  # [1 до 5] позже
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"