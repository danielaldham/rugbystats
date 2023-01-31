# Generated by Django 4.1.2 on 2023-01-31 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0014_player_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='result',
            field=models.CharField(choices=[('Win', 'Win'), ('Loss', 'Loss'), ('Draw', 'Draw')], default='Draw', max_length=4),
        ),
    ]