from django.db import models
from django.urls import reverse


# Create the game model
class Game(models.Model):

    # Override the default string to return the name of the game. Makes management easier
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('game-detail', args=[str(self.id)])
    
    title = models.CharField(max_length=50)
    description = models.TextField()

    # Path for coverart image 
    coverart = models.ImageField(upload_to="images/")

# Create the review model
class Review(models.Model):
    
    # Override the default string to return the name of the review.
    def __str__(self):
        return self.title
    
    # List of star choices
    RATING = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
        (6, '6 Stars'),
        (7, '7 Stars'),
        (8, '8 Stars'),
        (9, '9 Stars'),
        (10, '10 Stars'),
    )
    rating = models.IntegerField(choices=RATING)
    
    title = models.CharField(max_length=50)
    description = models.TextField()

    # one-to-many relationship w/ games. One game can have many reviews.
    game = models.ForeignKey(Game, on_delete=models.CASCADE, default = None)
