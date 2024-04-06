from django.db import models
from employees.models import Role

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    role = models.ForeignKey(Role, default=1, on_delete=models.CASCADE)

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
