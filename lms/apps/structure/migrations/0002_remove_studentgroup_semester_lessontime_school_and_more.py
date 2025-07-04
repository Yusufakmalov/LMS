# Generated by Django 5.2 on 2025-06-20 09:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_lesson_groups_lesson_about_lesson_text_and_more'),
        ('structure', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentgroup',
            name='semester',
        ),
        migrations.AddField(
            model_name='lessontime',
            name='school',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='lesson_times', to='main.school'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='science',
            name='school',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sciences', to='main.school'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sciencegroup',
            name='is_active',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studentgroup',
            name='academic_year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='groupmodel_to_academic_year', to='structure.academicyear'),
        ),
        migrations.AddField(
            model_name='studentgroup',
            name='is_active',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
