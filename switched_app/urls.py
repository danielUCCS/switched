from django.urls import path
from . import views

urlpatterns = [

    # Map index url to home page
    path('', views.index, name='index'),

    # Go the help page
    path('help/', views.help, name='help'),

    # Map to a detailed game view
    path('game/<int:pk>', views.GameDetailView.as_view(), name='game-detail'),

    # Create the review form
    path('game/<int:game_id>/create_review/', views.createReview, name='create-review'),

    # Update the review
    path('game/<int:game_id>/update_review/<int:review_id>', views.updateReview, name='update-review'),

    # Delete the review
    path('game/<int:game_id>/delete_review/<int:review_id>', views.deleteReview, name='delete-review'),

]