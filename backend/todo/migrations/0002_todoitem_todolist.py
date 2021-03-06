# Generated by Django 2.2.7 on 2019-11-14 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='blank title', max_length=200)),
                ('is_completed', models.BooleanField(default=False)),
                ('completed_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Todo List',
                'verbose_name_plural': 'Todo Lists',
                'ordering': ['name', 'created_at', 'is_completed'],
            },
        ),
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='blank title', max_length=200)),
                ('description', models.TextField(default='Blank text', max_length=200)),
                ('is_completed', models.BooleanField(default=False)),
                ('completed_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('deadline', models.DateTimeField()),
                ('todo_list', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.TodoList')),
            ],
            options={
                'verbose_name': 'Todo List',
                'verbose_name_plural': 'Todo Lists',
                'ordering': ['created_at', 'is_completed', 'deadline', 'name'],
            },
        ),
    ]
