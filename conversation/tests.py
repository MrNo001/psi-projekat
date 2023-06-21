from django.test import TestCase,Client
from django.urls import reverse
from offer.models import Offer, Picture
from account.models import User
from .models import ConversationMessage,Conversation
from search import views
from .forms import ConversationMessageForm

class ConversationModelTestCase(TestCase):
    def setUp(self):
        # Create test users for the conversation
        User.objects.all().delete()
        
        self.user1 = User.objects.create_user(username="user1")
        self.user2 = User.objects.create(username="user2")

        # Create a test offer for the conversation
        self.offer = Offer.objects.create(name="Test Offer")

      

    def test_conversation_creation(self):
        """
        Test that a Conversation instance can be created correctly.
        """
        conversation = Conversation.objects.create(offer=self.offer)
        conversation.members.add(self.user1, self.user2)
        conversation.save()

        self.assertEqual(conversation.offer, self.offer)
        self.assertEqual(conversation.members.count(), 2)

    def test_conversation_message_creation(self):
        """
        Test that a ConversationMessage instance can be created correctly.
        """
        conversation = Conversation.objects.create(offer=self.offer)
        conversation.members.add(self.user1, self.user2)
        conversation.save()

        message = ConversationMessage.objects.create(conversation=conversation, content="Test message", created_by=self.user1)

        self.assertEqual(message.conversation, conversation)
        self.assertEqual(message.content, "Test message")
        self.assertEqual(message.created_by, self.user1)

    def test_conversation_message_ordering(self):
        """
        Test that conversation messages are ordered by creation time.
        """
        conversation = Conversation.objects.create(offer=self.offer)
        conversation.members.add(self.user1, self.user2)
        conversation.save()

        message1 = ConversationMessage.objects.create(conversation=conversation, content="Message 1", created_by=self.user1)
        message2 = ConversationMessage.objects.create(conversation=conversation, content="Message 2", created_by=self.user2)

        messages = conversation.messages.all()
        self.assertEqual(messages[0], message1)
        self.assertEqual(messages[1], message2)




class ConversationViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.new_conversation_url = reverse('conversation:new', args=[1])  # Assuming offer_pk is 1
        self.inbox_url = reverse('conversation:inbox')
        self.detail_url = reverse('conversation:details', args=[1])  # Assuming conversation pk is 1

    def test_new_conversation_view(self):
        """
        Test the new_conversation view to ensure it creates a new conversation and redirects appropriately.
        """
        # Create a test user and offer
        user = User.objects.create_user(username='testuser', password='testpassword')
        offer = Offer.objects.create(created_by=User.objects.create_user(username='testfirm'), name='Test Offer')

        # Log in the user
        self.client.force_login(user)

        # Access the new_conversation view with a GET request
        response = self.client.get(self.new_conversation_url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the form in the response context is an instance of ConversationMessageForm
        self.assertIsInstance(response.context['form'], ConversationMessageForm)

        # Submit a POST request with valid form data
        response = self.client.post(self.new_conversation_url, {
            'content': 'Test message',
        })

        # Check that the response redirects to the offer details page
        self.assertRedirects(response, reverse('offer:details', args=[offer.pk]), status_code=302, target_status_code=200)

        # Check that a new conversation and message are created
        conversation = Conversation.objects.filter(offer=offer, members=user).first()
        self.assertIsNotNone(conversation)
        self.assertEqual(conversation.messages.count(), 1)
        self.assertEqual(conversation.messages.first().content, 'Test message')

    def test_inbox_view(self):
        """
        Test the inbox view to ensure it retrieves the conversations for the logged-in user.
        """
        # Create a test user and conversations
        user = User.objects.create_user(username='testuser', password='testpassword')
        user2 = User.objects.create_user(username='testuser2', password='testpassword2')
        conversation = Conversation.objects.create(offer=Offer.objects.create(created_by=User.objects.create_user(username='testfirm'), name='Test Offer'))
        conversation.members.add(user)
        conversation.members.add(user2)


        # Log in the user
        self.client.force_login(user)

        # Access the inbox view
        response = self.client.get(self.inbox_url)


        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the conversations are passed to the template context
        self.assertQuerysetEqual(response.context['conversations'], [conversation])

    def test_detail_view(self):
        """
        Test the detail view to ensure it retrieves the conversation and allows sending messages.
        """
        # Create a test user, conversation, and form data
        user = User.objects.create_user(username='testuser', password='testpassword')
        conversation = Conversation.objects.create(offer=Offer.objects.create(created_by=User.objects.create_user(username='testfirm'), name='Test Offer'))
        conversation.members.add(user)
        form_data = {'content': 'Test message'}

        # Log in the user
        self.client.force_login(user)

        # Access the detail view with a GET request
        response = self.client.get(self.detail_url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the form in the response context is an instance of ConversationMessageForm
        self.assertIsInstance(response.context['form'], ConversationMessageForm)

        # Submit a POST request with valid form data
        response = self.client.post(self.detail_url, form_data)

        # Check that the response redirects back to the detail view
        self.assertRedirects(response, reverse('conversation:details', args=[conversation.pk]), status_code=302, target_status_code=200)

        # Check that a new message is created for the conversation
        self.assertEqual(conversation.messages.count(), 1)
        self.assertEqual(conversation.messages.first().content, 'Test message')

