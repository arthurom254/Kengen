# Generated by Django 4.1.4 on 2023-05-14 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('campus', models.CharField(max_length=200)),
                ('emailaddress', models.CharField(max_length=100)),
                ('postbox', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['title', 'campus'],
            },
        ),
        migrations.CreateModel(
            name='LearningObjective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('activityDone', models.TextField(max_length=2000)),
                ('newSkillsAquired', models.TextField(max_length=2000)),
                ('challangesMet', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('learning_objective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attachment.learningobjective')),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attachment.department')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('refcode', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attachment.department')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attachment.institution')),
            ],
        ),
        migrations.CreateModel(
            name='ProgressUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_done', models.TextField()),
                ('lesson_learnt', models.TextField()),
                ('challenge_met', models.TextField()),
                ('weekly_progress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attachment.weeklyprogress')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attachment.logs')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
