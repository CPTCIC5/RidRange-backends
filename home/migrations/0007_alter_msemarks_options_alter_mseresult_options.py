# Generated by Django 5.1.2 on 2024-11-04 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_msemarks_course'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='msemarks',
            options={'verbose_name': 'mseMarks', 'verbose_name_plural': 'mseMarks'},
        ),
        migrations.AlterModelOptions(
            name='mseresult',
            options={'verbose_name': 'mseResult', 'verbose_name_plural': 'mseResult'},
        ),
    ]
