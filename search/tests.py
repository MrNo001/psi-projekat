from django.test import TestCase, Client
from django.urls import reverse
from offer.models import Offer, Picture
from .views import index, browse, about

class SearchViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('search:home')
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
        image1=Picture.objects.create(offer=offer1,image='testFolder/img.jpg')
        image2=Picture.objects.create(offer=offer2,image='testFolder/img.jpg')

        # Access the index view
        response = self.client.get(self.index_url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the premium offers are passed to the template context
        
     
        test=[{offer1,image1}, {offer2,image2}]

        dict=response.context['offers']
        list=[]
        for i in dict:
            list += [{i["offer"],i["image"]}]






        self.assertEqual(
            list,
            test,
        )

    def test_browse_view(self):
        """
        Test the browse view to ensure it filters offers correctly based on query parameters.
        """
        # Create test offers
        offer1 = Offer.objects.create(name='Offer 1', make='Make1', model='Model1', year=2000)
        offer2 = Offer.objects.create(name='Offer 2', make='Make2', model='Model2', year=2005)
        offer3 = Offer.objects.create(name='Offer 3', make='Make3', model='Model3', year=2010)
        image1=Picture.objects.create(offer=offer1,image='testFolder/img.jpg')
        image2=Picture.objects.create(offer=offer2,image='testFolder/img.jpg')
        image3=Picture.objects.create(offer=offer3,image='testFolder/img.jpg')
        


        # Access the browse view with query parameters
        response = self.client.get(self.browse_url, {'make': 'Make1', 'model': 'Model1', 'yearStart': '2000', 'yearEnd': '2005'})

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the filtered offers are passed to the template context
        self.assertEqual(
            response.context['offers'][0],
            {'offer':offer1,'image':image1}
        )

    def test_about_view(self):
        """
        Test the about view to ensure it returns the expected response.
        """
        # Access the about view
        response = self.client.get(self.about_url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

