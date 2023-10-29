from django.urls import path
from . import views

urlpatterns = [

    # Map index url to home page
    path('', views.index, name='index'),

    # Map to a detailed game view
    path('game/<int:pk>', views.GameDetailView.as_view(), name='game-detail'),

    # Create the review form
    path('game/<int:game_id>/create_review/', views.createReview, name='create-review'),

]