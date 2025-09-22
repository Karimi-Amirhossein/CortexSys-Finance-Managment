from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import CustomUser

class TestAccountRegistration(APITestCase):
    """Test user registration API."""

    def setUp(self):
        self.url = reverse('accounts:register')
        self.user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "a-Secure-Password-123",
            "first_name": "Test",
            "last_name": "User"
        }

    def test_register_creates_user(self):
        self.assertEqual(CustomUser.objects.count(), 0)

        response = self.client.post(self.url, self.user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)

        user = CustomUser.objects.get()
        self.assertEqual(user.username, self.user_data['username'])
        self.assertEqual(user.email, self.user_data['email'])
        self.assertTrue(user.check_password(self.user_data['password']))
        self.assertNotIn('password', response.data)
