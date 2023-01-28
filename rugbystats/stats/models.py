from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=30)
    invite_code = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=20, choices=[
        ('prop', 'Prop'),
        ('hooker', 'Hooker'),
        ('lock', 'Lock'),
        ('flanker', 'Flanker'),
        ('no8', 'No. 8'),
        ('scrum_half', 'Scrum Half'),
        ('fly_half', 'Fly Half'),
        ('centre', 'Centre'),
        ('wing', 'Wing'),
        ('full_back', 'Full Back')
    ])
    
    def __str__(self):
        return self.name


class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.ManyToManyField(Position)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)

    
    def __str__(self):
        return self.first_name + " " + self.last_name

    def full_name(self):
        return self.first_name + " " + self.last_name


class MyUser(AbstractUser):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, null=True, blank=True)
    coach = models.BooleanField(default=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)

    @property
    def is_coach(self):
        return self.coach

class Match(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    date = models.DateField()
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.home_team} vs {self.away_team}'
    
    def match_name(self):
        return f"{self.home_team.name} vs {self.away_team.name}"


class PlayerStatistic(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    started = models.BooleanField(default=False)
    tackles_made = models.IntegerField(default=0)
    rucks_hit = models.IntegerField(default=0)
    passes = models.IntegerField(default=0)
    carries = models.IntegerField(default=0)
    tackles_missed = models.IntegerField(default=0)
    tries = models.IntegerField(default=0)
    conversions = models.IntegerField(default=0)
    penalties = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.player.full_name()} - {self.match.home_team} vs {self.match.away_team} on {self.match.date}'