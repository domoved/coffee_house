from django.contrib.auth.models import User
from django.db import models

from coffee_house.roles import ROLE_CHOICES, ROLE_HIERARCHY


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    @property
    def role_hierarchy(self):
        return ROLE_HIERARCHY[self.role]

    def upgrade_role(self):
        if self.role == 'intern':
            self.role = 'barista'
        elif self.role == 'barista':
            self.role = 'manager'
        elif self.role == 'manager':
            self.role = 'supervisor'
        elif self.role == 'supervisor':
            self.role = 'hr_manager'
        self.save()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.user.username}"


class Document(models.Model):
    title = models.CharField(max_length=100)
    document = models.FileField(upload_to='documents/')
    document_type = models.CharField(max_length=100, default='')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.document_type = 'txt'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
