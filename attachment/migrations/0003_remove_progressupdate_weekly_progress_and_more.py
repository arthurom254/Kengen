# Generated by Django 4.1.4 on 2023-05-14 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attachment', '0002_logs_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='progressupdate',
            name='weekly_progress',
        ),
        migrations.RemoveField(
            model_name='weeklyprogress',
            name='learning_objective',
        ),
        migrations.DeleteModel(
            name='LearningObjective',
        ),
        migrations.DeleteModel(
            name='ProgressUpdate',
        ),
        migrations.DeleteModel(
            name='WeeklyProgress',
        ),
    ]
