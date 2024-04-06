# Generated by Django 5.0.4 on 2024-04-06 10:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='role',
            field=models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='employees.userprofile'),
        ),
    ]
