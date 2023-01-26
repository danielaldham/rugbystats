# Generated by Django 4.1.2 on 2023-01-26 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchStatistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tries', models.IntegerField(default=0)),
                ('conversions', models.IntegerField(default=0)),
                ('penalties', models.IntegerField(default=0)),
                ('started', models.BooleanField(default=False)),
                ('yellow_cards', models.IntegerField(default=0)),
                ('red_cards', models.IntegerField(default=0)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.player')),
            ],
        ),
    ]
