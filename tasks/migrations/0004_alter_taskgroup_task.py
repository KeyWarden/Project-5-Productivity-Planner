# Generated by Django 3.2.20 on 2023-07-29 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_taskgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskgroup',
            name='task',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='task_group', to='tasks.task'),
        ),
    ]
