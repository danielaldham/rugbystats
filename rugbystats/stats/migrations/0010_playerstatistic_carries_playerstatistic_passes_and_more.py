# Generated by Django 4.1.2 on 2023-01-26 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0009_rename_matchstatistic_playerstatistic'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerstatistic',
            name='carries',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='playerstatistic',
            name='passes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='playerstatistic',
            name='rucks_hit',
            field=models.IntegerField(default=0),
        ),
    ]
