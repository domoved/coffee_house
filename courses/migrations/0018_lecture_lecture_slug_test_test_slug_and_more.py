# Generated by Django 5.0.4 on 2024-04-08 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_remove_lecture_lecture_slug_remove_test_test_slug'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='course',
            name='course_slug',
            field=models.SlugField(default='', max_length=100, unique=True),
        ),
    ]
