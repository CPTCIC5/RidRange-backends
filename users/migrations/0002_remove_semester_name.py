# Generated by Django 5.1.2 on 2024-11-01 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester',
            name='name',
        ),
    ]
