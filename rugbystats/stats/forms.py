from django import forms
from .models import Player, Match

class AddPlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'position']


class AddMatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['home_team', 'away_team', 'date', 'home_score', 'away_score']

