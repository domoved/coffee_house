from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20)  # Стажер, бариста, менеджер и т. д.

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
