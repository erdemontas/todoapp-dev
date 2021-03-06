# Generated by Django 2.2.7 on 2019-11-14 18:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_auto_20191114_2136'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Todo',
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='completed_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 14, 21, 51, 33, 73605), null=True),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 14, 21, 51, 33, 73605), null=True),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='deadline',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 14, 21, 51, 33, 73605), null=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='completed_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 14, 21, 51, 33, 72606), null=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 14, 21, 51, 33, 72606), null=True),
        ),
    ]
