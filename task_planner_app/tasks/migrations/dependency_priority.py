# Generated by Django 3.2.13 on 2022-07-30 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20220719_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('5', 'Lowest'), ('4', 'Low'), ('3', 'Medium'), ('2', 'High'), ('1', 'Highest')], default='Lowest', max_length=8),
        ),
        migrations.CreateModel(
            name='TaskDependency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_task', to='tasks.task')),
                ('parent_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_task', to='tasks.task')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='linked_tasks',
            field=models.ManyToManyField(blank=True, through='tasks.TaskDependency', to='tasks.Task'),
        ),
    ]
