from django.test import TestCase,Client
from .models import User, Offer, Picture
from django.urls import reverse
from account.models import User
from .models import Offer, Picture
from .views import details, new, edit, delete

class OfferModelTestCase(TestCase):
    def setUp(self):
        # Create a test user for the offer
        self.user = User.objects.create(username="testuser")

    def test_offer_creation(self):
        """
        Test that an Offer instance can be created correctly.
        """
        offer = Offer.objects.create(
            name="Test Offer",
            description="Test description",
            make="Test Make",
            model="Test Model",
            year=2022,
            mileage=10000,
            body_type="L",
            fuel_type="B",
            gearbox="M",
            power=150,
            price=50000,
            created_by=self.user,
            is_premium=True,
            reported=False,
        )

        self.assertEqual(offer.name, "Test Offer")
        self.assertEqual(offer.description, "Test description")
        self.assertEqual(offer.make, "Test Make")
        self.assertEqual(offer.model, "Test Model")
        self.assertEqual(offer.year, 2022)
        self.assertEqual(offer.mileage, 10000)
        self.assertEqual(offer.body_type, "L")
        self.assertEqual(offer.fuel_type, "B")
        self.assertEqual(offer.gearbox, "M")
        self.assertEqual(offer.power, 150)
        self.assertEqual(offer.price, 50000)
        self.assertEqual(offer.created_by, self.user)
        self.assertTrue(offer.is_premium)
        self.assertFalse(offer.reported)

    def test_offer_string_representation(self):
        """
        Test that the __str__ method of Offer returns the expected string.
        """
        offer = Offer.objects.create(name="Test Offer", created_by=self.user)
        expected_string = "Test Offer"
        self.assertEqual(str(offer), expected_string)

class PictureModelTestCase(TestCase):
    def setUp(self):
        # Create a test user for the offer
        self.user = User.objects.create(username="testuser")
        # Create a test offer
        self.offer = Offer.objects.create(name="Test Offer", created_by=self.user)

    def test_picture_creation(self):
        """
        Test that a Picture instance can be created correctly.
        """
        picture = Picture.objects.create(
            image="path/to/image.jpg",
            offer=self.offer
        )

        self.assertEqual(picture.image, "path/to/image.jpg")
        self.assertEqual(picture.offer, self.offer)



class OfferViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.details_url = reverse('offer:details', kwargs={'pk': 1})
        self.new_url = reverse('offer:new')
        self.edit_url = reverse('offer:edit', kwargs={'pk': 1})
        self.delete_url = reverse('offer:delete', kwargs={'pk': 1})
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_details_view(self):
        """
        Test the details view to ensure it retrieves offer details correctly.
        """
        # Create a test offer
        offer = Offer.objects.create(name='Test Offer')

        # Access the details view
        response = self.client.get(self.details_url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the offer is passed to the template context
        self.assertEqual(response.context['offer'], offer)

    def test_new_view(self):
        """
        Test the new view to ensure it creates a new offer.
        """
        # Log in as the user
        self.client.force_login(self.user)

        # Access the new view
        response = self.client.get(self.new_url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Submit a POST request to create a new offer
        response = self.client.post(self.new_url, {'name': 'New Offer','make':'makeUpdated','description':'descriptionUpdated',
                                                   'model':'modelUpdated','year':1,'mileage':1,'body_type':'L','fuel_type':'B',
                                                    'gearbox':'M','power':0,'price':200})

        # Check that the response redirects to the details view of the created offer
        self.assertRedirects(response, reverse('offer:details', kwargs={'pk': 1}))

        # Check that the offer is created in the database
        self.assertEqual(Offer.objects.count(), 1)
        offer = Offer.objects.first()
        self.assertEqual(offer.name, 'New Offer')
        self.assertEqual(offer.created_by, self.user)

    def test_edit_view(self):
        """
        Test the edit view to ensure it updates an existing offer.
        """
        # Create a test offer
        offer = Offer.objects.create(name='Test Offer', created_by=self.user)

        # Log in as the user
        self.client.force_login(self.user)

        # Access the edit view
        response = self.client.get(self.edit_url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Submit a POST request to edit the offer
        response = self.client.post(self.edit_url,{'name': 'Updated Offer','make':'makeUpdated','description':'descriptionUpdated',
                                                   'model':'modelUpdated','year':1,'mileage':1,'body_type':'L','fuel_type':'B',
                                                    'gearbox':'M','power':0,'price':200})

        # Check that the response redirects to the details view of the edited offer
        self.assertRedirects(response, reverse('offer:details', kwargs={'pk': 1}))

        # Refresh the offer from the database
        offer.refresh_from_db()

        # Check that the offer is updated in the database
        self.assertEqual(offer.name, 'Updated Offer')

    def test_delete_view(self):
        """
        Test the delete view to ensure it deletes an existing offer.
        """
        # Create a test offer
        offer = Offer.objects.create(name='Test Offer', created_by=self.user)

        # Log in as the user
        self.client.force_login(self.user)

        # Submit a POST request to delete the offer
        response = self.client.post(self.delete_url)

        # Check that the response redirects to the home page
        self.assertRedirects(response, '/profil/')

        # Check that the offer is deleted from the database
        self.assertEqual(Offer.objects.count(), 0)

