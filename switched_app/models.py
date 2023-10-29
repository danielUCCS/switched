from django.db import models
from django.urls import reverse


# Create the game model
class Game(models.Model):

    # Override the default string to return the name of the game. Makes management easier
    def __str__(self):
        return self.title
    
    title = models.CharField(max_length=50)
    description = models.TextField()

    # Path for coverart image 
    coverart = models.ImageField(upload_to="images/")