# Generated by Django 5.0.4 on 2024-04-06 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='site_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='video_url',
            field=models.URLField(blank=True),
        ),
    ]