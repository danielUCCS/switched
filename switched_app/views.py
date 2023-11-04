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

# Help page
def help(request):
    return render (request, 'switched_app/help.html')

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

    # Update a project. We need both game and review id
def updateReview(request, game_id, review_id):
    game = Game.objects.get(pk=game_id)
    review = Review.objects.get(id=review_id)
    
    # Fill form with project instance
    form = ReviewForm(instance=review)

    # If request is POST
    if request.method == 'POST':

        # Update form
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            # Update the project
            form.save()

            # Redirect back to the portfolio detail page
            return redirect('game-detail', game_id)

    context = {'form': form}
    return render(request, 'switched_app/review_form.html', context)

# Delete a project from the database. Needs a portfolio id and project id
def deleteReview(request, game_id, review_id):
    
    # Filter desired project and portfolio objects
    review=Review.objects.filter(id=review_id)
    game=Game.objects.get(id=game_id)

    # If request is POST
    if request.method == 'POST':
        # Delete the object and return to portfolio page
        review.delete()
        return redirect('game-detail', game_id)
        
    # Send the game as context to render function
    context = {'item': game}
    return render(request, 'switched_app/delete_review.html', context)