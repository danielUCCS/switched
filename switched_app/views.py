from django.shortcuts import render
from django.shortcuts import redirect
from .models import Game
from .models import Review
from django.views import generic
from .forms import ReviewForm

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
    
# Form for creating a new review
def createReview(request, game_id):
    form = ReviewForm()
    game = Game.objects.get(pk=game_id)
    
    if request.method == 'POST':
        
        # If form is valid, pass in the request
        form = ReviewForm(request.POST)
        
        # If the form is valid, create a new project
        if form.is_valid():

            # Save the form without committing to the database
            review = form.save(commit=False)

            # Set the game relationship
            review.game = game
            review.save()

            # Redirect to portfolio detail page
            return redirect('game-detail', game_id)

    context = {'form': form}
    return render(request, 'switched_app/review_form.html', context)