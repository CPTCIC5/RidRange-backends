# Generated by Django 5.1.2 on 2024-11-01 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_courses_unique_together_courses_divisions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='division',
            name='name',
            field=models.CharField(max_length=10),
        ),
    ]