from django.contrib import admin
from .models import Match, MyUser, Player, Team

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Match)