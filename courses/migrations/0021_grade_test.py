# Generated by Django 5.0.4 on 2024-04-09 07:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0020_alter_course_course_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.test'),
        ),
    ]
