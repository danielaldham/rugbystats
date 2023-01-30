from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Q, Sum
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
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if len(password) < 8:
            return render(request, 'register.html', {'error': 'Password must be at least 8 characters'})

        if password == password2:
            if MyUser.objects.filter(username=username).exists():
                return render(request, 'register.html', {'error': 'Username already taken'})
            else:
                user = MyUser.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
                user.save()
                login(request, user)
                return redirect('index')
        else:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'register.html')


def index(request):
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
    user_team = request.user.team
    players = Player.objects.filter(team=user_team)
    stats = PlayerStatistic.objects.filter(player__in=players)
    squad_stats = {}
    for player in players:
        player_stats = stats.filter(player=player)
        squad_stats[player] = {
            'tackles_made': player_stats.aggregate(Sum('tackles_made'))['tackles_made__sum'] or 0,
            'rucks_hit': player_stats.aggregate(Sum('rucks_hit'))['rucks_hit__sum'] or 0,
            'passes': player_stats.aggregate(Sum('passes'))['passes__sum'] or 0,
            'carries': player_stats.aggregate(Sum('carries'))['carries__sum'] or 0,
            'tackles_missed': player_stats.aggregate(Sum('tackles_missed'))['tackles_missed__sum'] or 0,
            'tries': player_stats.aggregate(Sum('tries'))['tries__sum'] or 0,
            'conversions': player_stats.aggregate(Sum('conversions'))['conversions__sum'] or 0,
            'penalties': player_stats.aggregate(Sum('penalties'))['penalties__sum'] or 0,
            'yellow_cards': player_stats.aggregate(Sum('yellow_cards'))['yellow_cards__sum'] or 0,
            'red_cards': player_stats.aggregate(Sum('red_cards'))['red_cards__sum'] or 0,
        }
    top_tacklers = sorted(squad_stats.items(), key=lambda x: x[1]['tackles_made'], reverse=True)[:3]
    top_tries = sorted(squad_stats.items(), key=lambda x: x[1]['tries'], reverse=True)[:3]
    top_passes = sorted(squad_stats.items(), key=lambda x: x[1]['passes'], reverse=True)[:3]
    top_tacklers = sorted(squad_stats.items(), key=lambda x: x[1]['tackles_made'], reverse=True)[:3]
    top_rucks = sorted(squad_stats.items(), key=lambda x: x[1]['rucks_hit'], reverse=True)[:3]
    return render(request, 'squad_stats.html', {'squad_stats': squad_stats, 'top_tacklers': top_tacklers, 'top_tries': top_tries, 'top_passes': top_passes, 'top_rucks': top_rucks})

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

def about(request):
    return render(request, 'about.html')

def register_test(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        password1 = request.POST['password1']
