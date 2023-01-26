from django import forms
from .models import Player, Match, PlayerStatistic

class AddPlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'position']


class AddMatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['home_team', 'away_team', 'date', 'home_score', 'away_score']


class MatchStatisticForm(forms.ModelForm):
    class Meta:
        model = PlayerStatistic
        fields = ['match', 'player', 'tries', 'conversions', 'penalties', 'started', 'yellow_cards', 'red_cards', 'tackles_made', 'tackles_missed']
