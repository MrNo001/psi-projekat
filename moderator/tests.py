from django.test import TestCase, Client
from django.urls import reverse
from account.models import User
from offer.models import Offer, Picture
from .views import panel

class ModeratorViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.panel_url = reverse('moderator:panel')
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.userAdmin = User.objects.create_user(username='testuseradmin', password='testpassword', tip="A")

    def test_panel_view(self):
        """
        Test the panel view to ensure it retrieves reported offers correctly.
        """
        # Create a test offer with reported=True
        offer = Offer.objects.create(name='Test Offer', reported=True)
        Picture.objects.create(offer=offer,image="testFolder/img.jpg")

        # Log in as the user
        self.client.force_login(self.user)

        # Access the panel view
        response = self.client.get(self.panel_url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 403)

        # Check that the reported offers are passed to the template context
        self.assertQuerysetEqual(response.context['ReportedOffers'], [{'image': Picture.objects.filter(offer=offer).first(),'offer': offer}])

    def test_panel_view_admin(self):
        """
        Test the panel view to ensure it retrieves reported offers correctly.
        """
        # Create a test offer with reported=True
        offer = Offer.objects.create(name='Test Offer', reported=True)
        Picture.objects.create(offer=offer,image="testFolder/img.jpg")

        # Log in as the user
        self.client.force_login(self.userAdmin)

        # Access the panel view
        response = self.client.get(self.panel_url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the reported offers are passed to the template context
        self.assertQuerysetEqual(response.context['ReportedOffers'], [{'image': Picture.objects.filter(offer=offer).first(),'offer': offer}])

''' def test_report_ad_view(self):
        """
        Test the report_ad view to ensure it marks the offer as reported.
        """
        # Create a test offer
        offer = Offer.objects.create(name='Test Offer')

        # Log in as the user
        self.client.force_login(self.user)

        # Submit a POST request to report the offer
        response = self.client.post(self.report_ad_url, {'offer_id': offer.id})

        # Check that the response is a JSON response with success=True
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': True})

        # Refresh the offer from the database
        offer.refresh_from_db()

        # Check that the offer is marked as reported
        self.assertTrue(offer.reported)

    def test_follow_ad_view(self):
        """
        Test the follow_ad view to ensure it adds the user as a subscriber to the offer.
        """
        # Create a test offer
        offer = Offer.objects.create(name='Test Offer')

        # Log in as the user
        self.client.force_login(self.user)

        # Submit a POST request to follow the offer
        response = self.client.post(self.follow_ad_url, {'offer_id': offer.id})

        # Check that the response is a JSON response with success=True
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': True})

        # Refresh the offer from the database
        offer.refresh_from_db()

        # Check that the user is added as a subscriber to the offer
        self.assertIn(self.user, offer.subscribers.all())'''