from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('matches/', views.matches, name='matches'),
    path('squad/', views.squad_stats, name='squad'),
    path('players/', views.add_players, name='add_players'),
    path('add_match/', views.add_match, name='add_match'),
    path('join/', views.join_team, name='join'),
    path('match_stats/<int:match_id>/', views.player_statistics, name='player_statistics'),
]