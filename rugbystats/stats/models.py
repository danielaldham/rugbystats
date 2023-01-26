from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.CharField(max_length=20)
    pass

class Team(models.Model):
    name = models.CharField(max_length=30)

class MyUser(AbstractUser):
    coach = models.BooleanField(default=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)

class Match(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    date = models.DateField()
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)

class MatchStatistic(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    tries = models.IntegerField(default=0)
    conversions = models.IntegerField(default=0)
    penalties = models.IntegerField(default=0)
    started = models.BooleanField(default=False)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)
