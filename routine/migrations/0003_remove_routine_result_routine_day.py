# Generated by Django 4.0.2 on 2022-05-17 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0002_alter_routine_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routine_result',
            name='routine_day',
        ),
    ]
