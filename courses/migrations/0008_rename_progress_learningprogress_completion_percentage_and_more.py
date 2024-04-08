# Generated by Django 5.0.4 on 2024-04-07 17:52

import datetime

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_remove_course_site_url_course_slug_and_more'),
        ('employees', '0005_delete_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='learningprogress',
            old_name='progress',
            new_name='completion_percentage',
        ),
        migrations.RemoveField(
            model_name='test',
            name='answers',
        ),
        migrations.RemoveField(
            model_name='test',
            name='questions',
        ),
        migrations.AddField(
            model_name='certificationprocess',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
        migrations.AddField(
            model_name='course',
            name='users',
            field=models.ManyToManyField(through='courses.LearningProgress', to='employees.userprofile'),
        ),
        migrations.AlterField(
            model_name='learningprogress',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='learningprogress',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=250)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.test')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=250)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.question')),
            ],
        ),
    ]