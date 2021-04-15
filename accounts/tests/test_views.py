from django.test import TestCase, Client
from django.urls import resolve, reverse
from accounts.models import Users
from accounts.views import UserLoginView, UserLogoutView, SignUpView

class UserViewTests(TestCase):

    def setUp(self):
         Users.objects.create_user(
             username='test', 
             email='test@example.com',
             password='test')

    def test_login_view(self):
        #check login response
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)
        #check login process
        self.client = Client()
        login_status = self.client.login(email='test@example.com', password='test')
        self.assertTrue(login_status)

    def test_logout_view(self):
        response = self.client.get(reverse('accounts:logout'))
        self.assertEquals(response.status_code, 302)

        self.client = Client()
        login_status = self.client.logout()
        self.assertFalse(login_status)

    def test_signup_view(self):
        response = self.client.get(reverse('accounts:signup'))
        self.assertEqual(response.status_code, 200)
