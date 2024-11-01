# Generated by Django 5.1.2 on 2024-11-01 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_semester_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='courses',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='courses',
            name='divisions',
            field=models.ManyToManyField(to='users.division'),
        ),
        migrations.RemoveField(
            model_name='courses',
            name='division',
        ),
    ]
