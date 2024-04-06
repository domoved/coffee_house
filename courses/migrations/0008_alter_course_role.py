# Generated by Django 5.0.4 on 2024-04-06 09:22

import courses.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_course_role'),
        ('employees', '0005_alter_userprofile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='role',
            field=models.ForeignKey(default=courses.models.get_hr_manager_role_id, on_delete=django.db.models.deletion.CASCADE, to='employees.role'),
        ),
    ]
