from django.contrib import admin
from .models import Match, PlayerStatistic, MyUser, Player, Position, Team

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(PlayerStatistic)
admin.site.register(Position)