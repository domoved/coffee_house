# Generated by Django 5.0.4 on 2024-04-07 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_rename_progress_learningprogress_completion_percentage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerial',
            name='material_link',
            field=models.URLField(default='', null=True),
        ),
    ]
