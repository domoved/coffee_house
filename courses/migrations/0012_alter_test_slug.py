# Generated by Django 5.0.4 on 2024-04-08 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_lecture_slug_test_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='slug',
            field=models.SlugField(default='', max_length=100),
        ),
    ]
