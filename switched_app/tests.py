from django.test import TestCase
from django.urls import reverse
from .models import Game
from .models import Review

""" # Test the Game model
class ReviewTest(TestCase):
    def setUp(self):

        Review.objects.create(rating=3, title='TEST REVIEW', description='Test review description', game_id = 1)

    def test_review(self):

        TestReview = Review.objects.get(title='TEST GAME')
        self.assertEqual(TestReview.rating, 3)
        self.assertEqual(TestReview.title, 'TEST GAME')
        self.assertEqual(TestReview.description, 'Test review description')
        self.assertEqual(TestReview.game_id, 1)


# Create your tests here. 
class GameDetailViewTest(TestCase):
    def setUp(self):

        Game.objects.create(title='TEST GAME', description='Test game description')

    def test_game_detail_view(self):

        TestGame = Game.objects.get(title='TEST GAME')
        self.assertEqual(TestGame.status_code, 200)
        self.assertTemplateUsed(TestGame, 'switched_app/game_detail.html')
        self.assertContains(TestGame, 'Test Post') """
