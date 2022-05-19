# Generated by Django 3.2.13 on 2022-05-17 13:24

from django.db import migrations, models
import django.db.models.deletion
import task_manager_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ToDoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField(default=task_manager_app.models.one_week_task)),
                ('todo_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_manager_app.todolist')),
            ],
            options={
                'ordering': ['due_date'],
            },
        ),
    ]
