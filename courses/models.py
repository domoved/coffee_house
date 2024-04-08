from datetime import datetime

from django.db import models
from django.utils.text import slugify
from unidecode import unidecode

from coffee_house.roles import ROLE_CHOICES, ROLE_HIERARCHY
from employees.models import UserProfile


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    video_url = models.URLField(blank=True)
    course_slug = models.SlugField(unique=True, max_length=100, default='')
    users = models.ManyToManyField(UserProfile, through='LearningProgress')

    @property
    def role_hierarchy(self):
        return ROLE_HIERARCHY[self.role]

    def save(self, *args, **kwargs):
        if not self.course_slug or self.course_slug != slugify(unidecode(self.title)):
            self.course_slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Lecture(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lecture_slug = models.SlugField(unique=True, max_length=100, default='')

    def save(self, *args, **kwargs):
        if not self.lecture_slug or self.lecture_slug != slugify(unidecode(self.title)):
            self.lecture_slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Test(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    test_slug = models.SlugField(unique=True, max_length=100, default='')

    def save(self, *args, **kwargs):
        if not self.test_slug or self.test_slug != slugify(unidecode(self.title)):
            self.test_slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=250)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=250)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question} - {self.answer_text}"


class LearningProgress(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    completion_percentage = models.IntegerField(default=0)
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(default=datetime.now)
    is_complete = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.completion_percentage == 100:
            self.is_complete = True
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} - {self.course}"


class CourseMaterial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()
    material_link = models.URLField(null=True, default='')

    def __str__(self):
        return self.course.title


class CertificationProcess(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    certification_passed = models.BooleanField()
    certification_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user} - {self.certification_passed}"


class Grade(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.IntegerField()
    date_assigned = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'course']

    def __str__(self):
        return f"{self.user} - {self.course} - {self.grade}"
