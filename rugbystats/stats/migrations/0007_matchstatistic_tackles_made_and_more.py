# Generated by Django 4.1.2 on 2023-01-26 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0006_alter_team_invite_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchstatistic',
            name='tackles_made',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='matchstatistic',
            name='tackles_missed',
            field=models.IntegerField(default=0),
        ),
    ]
