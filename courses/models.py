from django.db import models

from employees.models import UserProfile


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ROLE_CHOICES = (
        ('intern', 'Стажер'),
        ('barista', 'Бариста'),
        ('manager', 'Менеджер'),
        ('supervisor', 'Управляющий'),
        ('hr_manager', 'Менеджер по персоналу'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    video_url = models.URLField(blank=True)
    site_url = models.URLField(blank=True)

    def role_hierarchy(self):
        if self.role == 'hr_manager':
            return ['hr_manager']
        elif self.role == 'supervisor':
            return ['supervisor', 'hr_manager']
        elif self.role == 'manager':
            return ['manager', 'supervisor', 'hr_manager']
        elif self.role == 'barista':
            return ['barista', 'manager', 'supervisor', 'hr_manager']
        elif self.role == 'intern':
            return ['intern', 'barista', 'manager', 'supervisor', 'hr_manager']

    def __str__(self):
        return self.title


class Lecture(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Test(models.Model):
    title = models.CharField(max_length=100)
    questions = models.TextField()
    answers = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
