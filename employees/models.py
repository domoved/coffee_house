from django.contrib.auth.models import User
from django.db import models

from coffee_house.roles import ROLE_CHOICES, ROLE_HIERARCHY


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    @property
    def role_hierarchy(self):
        return ROLE_HIERARCHY[self.role]

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.user.username}"
