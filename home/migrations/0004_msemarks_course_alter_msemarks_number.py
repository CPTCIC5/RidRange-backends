# Generated by Django 5.1.2 on 2024-11-02 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_msemarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='msemarks',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.mseresult'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='msemarks',
            name='number',
            field=models.IntegerField(),
        ),
    ]