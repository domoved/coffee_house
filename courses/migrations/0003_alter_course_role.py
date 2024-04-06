# Generated by Django 5.0.4 on 2024-04-06 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='role',
            field=models.CharField(choices=[('intern', 'Стажер'), ('barista', 'Бариста'), ('manager', 'Менеджер'), ('supervisor', 'Управляющий'), ('hr_manager', 'Менеджер по персоналу')], max_length=20),
        ),
    ]