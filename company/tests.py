from django.test import TestCase,Client
from .models import User, Review, Offer
from django.urls import reverse
from django.contrib.auth.models import User
from .models import User as CustomUser, Review
from .forms import SignupForm, RateForm

class ReviewModelTestCase(TestCase):
    def setUp(self):
        # Create test users for the review
        self.user = User.objects.create(username="testuser")
        self.firm = User.objects.create(username="testfirm")

        # Create a test offer for the review
        self.offer = Offer.objects.create(title="Test Offer")

    def test_review_creation(self):
        """
        Test that a Review instance can be created correctly.
        """
        review = Review.objects.create(user=self.user, firm=self.firm, offer=self.offer, text="Test review", rate=4)
        self.assertEqual(review.user, self.user)
        self.assertEqual(review.firm, self.firm)
        self.assertEqual(review.offer, self.offer)
        self.assertEqual(review.text, "Test review")
        self.assertEqual(review.rate, 4)
        self.assertEqual(review.likes, 0)
        self.assertEqual(review.unlikes, 0)

    def test_review_string_representation(self):
        """
        Test that the __str__ method of Review returns the expected string.
        """
        review = Review.objects.create(user=self.user, firm=self.firm, offer=self.offer, text="Test review", rate=4)
        expected_string = self.user.username
        self.assertEqual(str(review), expected_string)



class CompanyViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.plac_url = reverse('company:plac', args=['testfirm'])
        self.rate_url = reverse('company:rate', args=['testfirm'])

    def test_plac_view(self):
        """
        Test the plac view to ensure it renders the plac template and retrieves the reviews for the specified firm.
        """
        # Create a test user and firm
        user = User.objects.create_user(username='testuser', password='testpassword')
        firm = User.objects.create_user(username='testfirm', password='testpassword')
        
        # Create a test review for the firm
        review = Review.objects.create(user=user, firm=firm)

        # Access the plac view
        response = self.client.get(self.plac_url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the reviews are passed to the template context
        self.assertQuerysetEqual(response.context['reviews'], [f"{{'review': {review}}}"])

    def test_rate_view(self):
        """
        Test the rate view to ensure it renders the rate template and saves a new review for the specified firm.
        """
        # Create a test user and firm
        user = User.objects.create_user(username='testuser', password='testpassword')
        firm = User.objects.create_user(username='testfirm', password='testpassword')
        
        # Log in the user
        self.client.force_login(user)

        # Access the rate view with a GET request
        response = self.client.get(self.rate_url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the form in the response context is an instance of RateForm
        self.assertIsInstance(response.context['form'], RateForm)

        # Submit a POST request with valid form data
        response = self.client.post(self.rate_url, {
            'rate': 5,
            'text': 'Test review',
        })

        # Check that the response redirects to the plac page for the specified firm
        self.assertRedirects(response, self.plac_url, status_code=302, target_status_code=200)

        # Check that a new review is created for the firm
        self.assertTrue(Review.objects.filter(user=user, firm=firm, rate=5, text='Test review').exists())

