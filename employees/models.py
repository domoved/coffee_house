from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Role(models.Model):
    ROLE_CHOICES = (
        ('intern', 'Стажер'),
        ('barista', 'Бариста'),
        ('manager', 'Менеджер'),
        ('supervisor', 'Управляющий'),
        ('hr_manager', 'Менеджер по персоналу'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.role

    @classmethod
    def get_hr_manager_role_id(cls):
        hr_manager_role = cls.objects.get(role='hr_manager')
        return hr_manager_role.id


class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('intern', 'Стажер'),
        ('barista', 'Бариста'),
        ('manager', 'Менеджер'),
        ('supervisor', 'Управляющий'),
        ('hr_manager', 'Менеджер по персоналу'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.user.username}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        role = 'intern'
        UserProfile.objects.create(user=instance, role=role)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
