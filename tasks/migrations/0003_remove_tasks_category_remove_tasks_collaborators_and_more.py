# Generated by Django 5.0 on 2023-12-07 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_tasks_category_tasks_collaborators_tasks_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='category',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='collaborators',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='description',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='priority',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='user',
        ),
        migrations.AlterField(
            model_name='tasks',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]