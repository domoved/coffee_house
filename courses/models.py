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


class LearningProgress(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.course}"


class CourseMaterial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()
    material_link = models.URLField()

    def __str__(self):
        return self.course.title


class CertificationProcess(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    certification_passed = models.BooleanField()
    certification_result = models.CharField(max_length=100)
    certification_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user} - {self.certification_result}"


class Grade(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.IntegerField()
    date_assigned = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.course} - {self.grade}"
