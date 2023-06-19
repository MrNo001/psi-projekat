from django.test import TestCase,Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import User as CustomUser
from .forms import SignupForm
from offer.models import Offer, Picture

from .models import User

class UserModelTestCase(TestCase):
    def test_user_creation(self):
        """
        Test that a User instance can be created correctly.
        """
        user = User.objects.create(username="testuser", email="test@example.com", tip="K")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.tip, "K")

    def test_user_default_type(self):
        """
        Test that the default user type is set correctly.
        """
        user = User.objects.create(username="testuser", email="test@example.com")
        self.assertEqual(user.tip, "K")

    def test_user_type_choices(self):
        """
        Test that the user type choices are enforced correctly.
        """
        user = User.objects.create(username="adminuser", email="admin@example.com", tip="A")
        self.assertEqual(user.tip, "A")

        # with self.assertRaises(ValueError):
        #     user = User.objects.create(username="invaliduser", email="invalid@example.com", tip="X")


class AccountViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('account:signup')
        self.dashboard_url = reverse('account:dashboard')
        self.edit_profile_url = reverse('account:edit_profile')
        self.logout_url = reverse('account:logout')

    def test_signup_view(self):
        """
        Test the signup view to ensure it renders the signup template and creates a new user.
        """
        # Submit a POST request with valid form data
        response = self.client.post(self.signup_url, {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
        })

        # Check that the response redirects to the login page
        self.assertRedirects(response, '/login/', status_code=302, target_status_code=200)

        # Check that a new user is created in the database
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_dashboard_view(self):
        """
        Test the dashboard view to ensure it renders the dashboard template and retrieves the user's offers and tracked offers.
        """
        # Create a test user and log them in
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(user)

        # Create a test offer and associate it with the user
        offer = Offer.objects.create(name='Test Offer', created_by=user)

        # Create a test picture and associate it with the offer
        picture = Picture.objects.create(image='path/to/image.jpg', offer=offer)

        # Access the dashboard view
        response = self.client.get(self.dashboard_url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the user's offers and tracked offers are passed to the template context
        self.assertQuerysetEqual(response.context['myOffers'], [f"{{'offer': {offer}, 'image': {picture}}}"])
        self.assertQuerysetEqual(response.context['trackedOffers'], [])

    def test_edit_profile_view(self):
        """
        Test the editProfile view to ensure it renders the edit template and updates the user's profile.
        """
        # Create a test user and log them in
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(user)

        # Access the editProfile view with a GET request
        response = self.client.get(self.edit_profile_url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the form in the response context is an instance of SignupForm
        self.assertIsInstance(response.context['form'], SignupForm)

        # Submit a POST request with updated form data
        response = self.client.post(self.edit_profile_url, {
            'username': 'newusername',
            'password1': 'newpassword',
            'password2': 'newpassword',
        })

        # Check that the response redirects to the dashboard page
        self.assertRedirects(response, self.dashboard_url, status_code=302, target_status_code=200)

        # Check that the user's profile is updated
        self.assertEqual(CustomUser.objects.get(id=user.id).username, 'newusername')

    def test_logout_view(self):
        """
        Test the logoutuser view to ensure it logs out the user and redirects to the index page.
        """
        # Create a test user and log them in
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(user)

        # Access the logoutuser view
        response = self.client.get(self.logout_url)

        # Check that the response redirects to the index page
        self.assertRedirects(response, reverse('search:index'), status_code=302, target_status_code=200)

        # Check that the user is logged out
        self.assertFalse(response.wsgi_request.user.is_authenticated)