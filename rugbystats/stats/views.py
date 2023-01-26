from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import MyUser, Match, Team, Player

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
    return render(request, 'index.html')

def matches(request):
    if request.user.is_authenticated:
        team = request.user.team
        matches = Match.objects.filter(home_team=team) | Match.objects.filter(away_team=team)
        context = {'matches': matches}
        return render(request, 'matches.html', context)
    else:
        return render(request, 'matches.html')

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
