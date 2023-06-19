from django.test import TestCase, Client
from django.urls import reverse
from .models import Offer, Picture
from .views import index, browse, about

class SearchViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('search:index')
        self.browse_url = reverse('search:browse')
        self.about_url = reverse('search:about')

    def test_index_view(self):
        """
        Test the index view to ensure it retrieves premium offers correctly.
        """
        # Create test offers
        offer1 = Offer.objects.create(name='Premium Offer 1', is_premium=True)
        offer2 = Offer.objects.create(name='Premium Offer 2', is_premium=True)
        offer3 = Offer.objects.create(name='Non-Premium Offer', is_premium=False)

        # Access the index view
        response = self.client.get(self.index_url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the premium offers are passed to the template context
        self.assertQuerysetEqual(
            response.context['offers'],
            [repr(offer1), repr(offer2)],
            ordered=False
        )

    def test_browse_view(self):
        """
        Test the browse view to ensure it filters offers correctly based on query parameters.
        """
        # Create test offers
        offer1 = Offer.objects.create(name='Offer 1', make='Make1', model='Model1', year=2000)
        offer2 = Offer.objects.create(name='Offer 2', make='Make2', model='Model2', year=2005)
        offer3 = Offer.objects.create(name='Offer 3', make='Make3', model='Model3', year=2010)

        # Access the browse view with query parameters
        response = self.client.get(self.browse_url, {'make': 'Make1', 'model': 'Model1', 'yearStart': '2000', 'yearEnd': '2005'})

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the filtered offers are passed to the template context
        self.assertQuerysetEqual(
            response.context['offers'],
            [repr(offer1)],
            ordered=False
        )

    def test_about_view(self):
        """
        Test the about view to ensure it returns the expected response.
        """
        # Access the about view
        response = self.client.get(self.about_url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the response content is the expected string
        self.assertEqual(response.content.decode(), 'O nama')

