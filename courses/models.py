from django.db import models
from employees.models import Role


def get_hr_manager_role_id():
    hr_manager_role = Role.objects.get(name='hr_manager')
    return hr_manager_role.id


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    role = models.CharField(max_length=100,
                            choices=[('intern', 'Стажер'), ('barista', 'Бариста'), ('manager', 'Менеджер'),
                                     ('supervisor', 'Управляющий'), ('hr_manager', 'Менеджер по персоналу')],
                            default='hr_manager')

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
