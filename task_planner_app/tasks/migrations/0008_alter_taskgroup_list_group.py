# Generated by Django 3.2.13 on 2022-07-16 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_group_model_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskgroup',
            name='list_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.taskgroup'),
        ),
    ]