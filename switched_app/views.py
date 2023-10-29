from django.shortcuts import render
from .models import Game
from .models import Review
from django.views import generic

# Home page
def index(request):
    games = Game.objects.all() # Generate queryset of all game objects 
    return render (request, 'switched_app/index.html', {'games':games}) # Convert games to dict and pass as context. Not entirely sure how that works...

class GameDetailView(generic.DetailView):
    model = Game

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(GameDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['review_list'] = Review.objects.filter(game_id=self.object.id)
        return context