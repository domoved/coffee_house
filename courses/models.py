from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class Lecture(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Test(models.Model):
    title = models.CharField(max_length=100)
    questions = models.TextField()
    answers = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
