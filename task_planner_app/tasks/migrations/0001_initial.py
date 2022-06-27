# Generated by Django 3.2.13 on 2022-06-27 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('list_group', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.taskgroup')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='', max_length=2000)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('S1', 'To do'), ('S2', 'In progress'), ('S3', 'Review'), ('S4', 'Complete')], default='TO_DO', max_length=8)),
                ('priority', models.CharField(choices=[('LOWEST', 'Lowest'), ('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High'), ('HIGHEST', 'Highest')], default='LOWEST', max_length=8)),
                ('assignee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('task_list', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.tasklist')),
            ],
            options={
                'ordering': ['status', '-priority', django.db.models.expressions.OrderBy(django.db.models.expressions.F('deadline'), nulls_last=True)],
            },
        ),
    ]
