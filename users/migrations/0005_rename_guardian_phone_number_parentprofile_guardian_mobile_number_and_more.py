# Generated by Django 5.1.2 on 2024-11-01 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_division_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parentprofile',
            old_name='guardian_phone_number',
            new_name='guardian_mobile_number',
        ),
        migrations.AlterField(
            model_name='semester',
            name='semester_number',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]),
        ),
    ]
