from django.shortcuts import render
from Store.models import *

def index(request):
    games = Games.objects.all()
    context = {
        'Games': games
    }
    return render(request, template_name='Store/index.html', context=context)

def game(request, id):
    game = Games.objects.get(pk=id)
    context = {
        'Game': game
    }
    return render(request, template_name='Store/game.html', context=context)