from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Q
from django_filters.views import FilterView

from django import forms

from .forms import AddMatchForm, AddPlayerForm

from .models import MyUser, Match, Team, Player, PlayerStatistic

# Create your views here.
class MyRegistrationForm(UserCreationForm):
    coach = forms.BooleanField(required=False)

    class Meta:
        model = MyUser
        fields = ['username', 'password1', 'password2', 'coach']

def register(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.coach = form.cleaned_data.get('coach')
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = MyRegistrationForm()
    return render(request, 'register.html', {'form': form})

def index(request):
    if request.user.is_authenticated:
        try:
            player = request.user.player
            statistics = PlayerStatistic.objects.filter(player=player)
            context = {'statistics': statistics}
            return render(request, 'index.html', context)
        except Player.DoesNotExist:
            context = {'message': 'You are not associated with a player. Please contact your coach to connect your account.'}
            return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')



def matches(request):
    user_team = request.user.team
    matches = Match.objects.filter(Q(home_team=user_team) | Q(away_team=user_team))
    return render(request, 'matches.html', {'matches': matches})


def squad_stats(request):
    team = Team.objects.get(user=request.user)
    players = Player.objects.filter(team=team)
    context = {'players': players}
    return render(request, 'squad_stats.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def add_players(request):
    if request.method == 'POST':
        form = AddPlayerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Player added successfully!')
            return redirect('add_players')
        else:
            messages.error(request, 'An error occurred. Please try again.')
    else:
        form = AddPlayerForm()
    return render(request, 'add_players.html', {'form': form})


def add_match(request):
    if request.method == 'POST':
        form = AddMatchForm(request.POST)
        if form.is_valid():
            match = form.save()
            messages.success(request, 'Match added successfully!')
            return redirect('matches')
        else:
            messages.error(request, 'An error occurred. Please try again.')
    else:
        form = AddMatchForm()
    return render(request, 'add_match.html', {'form': form})


def join_team(request):
    if request.method == 'POST':
        invite_code = request.POST.get('invite_code')
        try:
            team = Team.objects.get(invite_code=invite_code)
            request.user.team = team
            request.user.save()
            messages.success(request, 'You have successfully joined the team.')
            return redirect('index')
        except Team.DoesNotExist:
            messages.error(request, 'Invalid invite code. Please try again.')
    return render(request, 'join_team.html')

def player_statistics(request, match_id):
    match = Match.objects.get(id=match_id)
    statistics = PlayerStatistic.objects.filter(match=match)
    return render(request, 'player_statistics.html', {'statistics': statistics, 'match': match})