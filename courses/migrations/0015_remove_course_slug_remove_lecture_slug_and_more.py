# Generated by Django 5.0.4 on 2024-04-08 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_alter_lecture_slug_alter_test_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='test',
            name='slug',
        ),
        migrations.AddField(
            model_name='course',
            name='course_slug',
            field=models.SlugField(default='', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='lecture',
            name='lecture_slug',
            field=models.SlugField(default='', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='test',
            name='test_slug',
            field=models.SlugField(default='', max_length=100, unique=True),
        ),
    ]