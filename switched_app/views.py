from django.shortcuts import render
from .models import Game

# Home page
def index(request):
    games = Game.objects.all() # Generate queryset of all game objects 
    return render (request, 'switched_app/index.html', {'games':games}) # Convert games to dict and pass as context. Not entirely sure how that works...