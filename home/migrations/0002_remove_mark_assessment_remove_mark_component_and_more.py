# Generated by Django 5.1.2 on 2024-11-02 14:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('users', '0007_delete_usersemesterdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mark',
            name='assessment',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='component',
        ),
        migrations.CreateModel(
            name='mseResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mse_number', models.IntegerField(choices=[(1, 'MSE-1'), (2, 'MSE-2'), (3, 'MSE-3'), (4, 'MSE-4')])),
                ('result_day', models.DateTimeField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.courses')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.semester')),
            ],
        ),
        migrations.DeleteModel(
            name='Assessment',
        ),
        migrations.DeleteModel(
            name='AssessmentComponent',
        ),
        migrations.DeleteModel(
            name='Mark',
        ),
    ]
