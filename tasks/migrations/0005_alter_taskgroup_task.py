# Generated by Django 3.2.20 on 2023-07-29 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_taskgroup_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskgroup',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_group', to='tasks.task'),
        ),
    ]