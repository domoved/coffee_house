from django.contrib.auth.models import User
from django.db import models

from courses.models import Course


class LearningProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')
    document_type = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class CourseMaterial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()
    material_link = models.URLField()

    def __str__(self):
        return self.course


class CertificationProcess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    certification_passed = models.BooleanField()
    certification_result = models.CharField(max_length=100)
    certification_date = models.DateTimeField()

    def __str__(self):
        return self.certification_result


class Grade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.IntegerField()

    def __str__(self):
        return self.grade
