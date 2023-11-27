from django.test import TestCase
from django.urls import reverse
from .models import Game
from .models import Review
from django.contrib.auth.models import User

from .forms import ReviewForm
from .forms import CreateUserForm

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# Test the game model
class GameTestCase(TestCase):
    def setUp(self):
        Game.objects.create(title="test game with image", description="test game description", coverart="images/testimage.gif") # Image specified
        Game.objects.create(title="test game without image", description="test game description") # Image not specified

    def test_game(self):
        TestGameImage = Game.objects.get(id=1)
        TestGameNoImage = Game.objects.get(id=2)
        self.assertEqual(TestGameImage.title, "test game with image") 
        self.assertEqual(TestGameImage.description , "test game description") 
        self.assertEqual(TestGameImage.coverart.url, "/images/images/testimage.gif") # Verify that uploaded image used
        self.assertEqual(TestGameNoImage.title, "test game without image") 
        self.assertEqual(TestGameNoImage.description , "test game description") 
        self.assertEqual(TestGameNoImage.coverart.url, "/images/images/default.gif") # Verify that default image used

    def test_game_object_name(self):
        TestGameImage = Game.objects.get(id=1)
        self.assertEqual(str(TestGameImage), TestGameImage.title)

    def test_game_absolute_url(self):
        TestGameImage = Game.objects.get(id=1)
        self.assertEqual(TestGameImage.get_absolute_url(), '/game/1')

# Test the review model
class ReviewTest(TestCase):
    def setUp(self):
        Review.objects.create(rating=3, title='TEST REVIEW', description='Test review description', game_id = 1)
        Review.game = Game.objects.create(title="test game", description="test game description") # Establish relationship with game model

    def test_review(self):
        TestReview = Review.objects.get(id=1)
        TestGame = Game.objects.get(title="test game")
        self.assertEqual(TestReview.rating, 3)
        self.assertEqual(TestReview.title, 'TEST REVIEW')
        self.assertEqual(TestReview.description, 'Test review description')
        self.assertEqual(TestReview.game_id, TestGame.id)

    def test_review_object_name(self):
        TestReview = Review.objects.get(id=1)
        self.assertEqual(str(TestReview), TestReview.title)

# Test the form for creating a new review
class ReviewFormTest(TestCase):
    def setUp(self):
        Review.objects.create(rating=1, title='TEST REVIEW', description='Test review description', game_id = 1)
        Review.game = Game.objects.create(title="test game", description="test game description") # Establish relationship with game model

    def test_valid_form(self):
        TestReview = Review.objects.get(id=1)
        data = {'title':TestReview.title, 'description':TestReview.description, 'rating':TestReview.rating,}
        form = ReviewForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        TestReview = Review.objects.get(id=1)
        data = {'title':TestReview.title, 'description':TestReview.description,}
        form = ReviewForm(data=data)
        self.assertFalse(form.is_valid())

# Test signing up for account 
class SignUpTest(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_valid_signup(self): 
        # Visit home page
        self.driver.get(self.live_server_url)

        # Visit the page signing up
        self.driver.find_element(By.LINK_TEXT, "Sign Up").click()

        # Enter valid data for account creation
        self.driver.find_element(By.ID, 'id_username').send_keys("test_user")
        self.driver.find_element(By.ID, "id_email").send_keys("email@mail.com")
        self.driver.find_element(By.ID, "id_password1").send_keys("passwd123")
        self.driver.find_element(By.ID, "id_password2").send_keys("passwd123")

        self.driver.find_element(By.ID, "id_submit").click()

        # See if successful account creation message is present
        body_text = self.driver.find_element(By.TAG_NAME, "body").text

        self.assertTrue("Successfully added account for test_user" in body_text)

    def test_invalid_signup(self): 
        # Visit home page
        self.driver.get(self.live_server_url)

        # Visit the page signing up
        self.driver.find_element(By.LINK_TEXT, "Sign Up").click()

        # Enter valid data for account creation
        self.driver.find_element(By.ID, 'id_username').send_keys("test_user")
        self.driver.find_element(By.ID, "id_email").send_keys("email@mail.com")
        self.driver.find_element(By.ID, "id_password1").send_keys("passwd123")
        self.driver.find_element(By.ID, "id_password2").send_keys("passwd1234")

        self.driver.find_element(By.ID, "id_submit").click()

        # See if successful account creation message is present
        body_text = self.driver.find_element(By.TAG_NAME, "body").text

        self.assertTrue("The two password fields didn’t match" in body_text)

    def tearDown(self):
        self.driver.quit()

# Test loggin into account
class LoginTest(LiveServerTestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test_user", password="passwd123")
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(2)

    def test_valid_login(self):
        
        # Visit home page
        self.driver.get(self.live_server_url)

        # Visit login page
        self.driver.find_element(By.LINK_TEXT, "Login").click()

        # Log into account
        self.driver.find_element(By.ID, 'id_username').send_keys("test_user")
        self.driver.find_element(By.ID, "id_password").send_keys("passwd123")
        self.driver.find_element(By.ID, "id_login").click()

        # See if successful login
        body_text = self.driver.find_element(By.TAG_NAME, "body").text

        self.assertTrue("Logout test_user" in body_text)

    def test_invalid_login(self):
        
        # Visit home page
        self.driver.get(self.live_server_url)

        # Visit login page
        self.driver.find_element(By.LINK_TEXT, "Login").click()

        # Log into account
        self.driver.find_element(By.ID, 'id_username').send_keys("test_user")
        self.driver.find_element(By.ID, "id_password").send_keys("passwd1234")
        self.driver.find_element(By.ID, "id_login").click()

        # See if successful login
        body_text = self.driver.find_element(By.TAG_NAME, "body").text

        self.assertTrue("Your username and password didn't match. Please try again." in body_text)

    def tearDown(self):
        self.driver.quit()

# adding something to test coverage
