# Generated by Django 3.0.6 on 2020-05-20 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='accomplished',
            field=models.BooleanField(default=False),
        ),
    ]
