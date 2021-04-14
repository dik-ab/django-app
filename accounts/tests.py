from django.test import TestCase, Client
from django.urls import resolve, reverse
from .models import Users
from .views import UserLoginView, UserLogoutView, SignUpView

class UsersModelTests(TestCase):
    
    def test_is_empty(self):
        saved_users = Users.objects.all()
        self.assertEqual(saved_users.count(), 0)

    def test_user_is_not_empty(self):
        user = Users(username="test_user", email='test@example.com', is_active=True, is_staff=False)
        user.save()
        saved_user = Users.objects.all()
        self.assertEqual(saved_user.count(), 1)

    def test_saving_and_retrieving_user(self):
        user = Users()
        username = 'test_user'
        email = 'test@example.com'
        is_active = True
        is_staff = False
        user.username = username
        user.email = email
        user.is_active = is_active
        user.is_staff = is_staff
        user.save()

        saved_user = Users.objects.all()
        actual_user = saved_user[0]

        self.assertEqual(actual_user.username, username)
        self.assertEqual(actual_user.username, username)


class TestUrls(TestCase):

    def test_user_login_url(self):
        view = resolve('/accounts/login/')
        self.assertEqual(view.func.view_class, UserLoginView)
    
    def test_user_logout_url(self):
        view = resolve('/accounts/logout/')
        self.assertEqual(view.func.view_class, UserLogoutView)

    def test_user_signup_url(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.view_class, SignUpView)



class UserLoginAndLogoutTests(TestCase):

    def setUp(self):
         Users.objects.create_user(
             username='test', 
             email='test@example.com',
             password='test')

    def test_login(self):
        #check login response
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)
        #check login process
        self.client = Client()
        login_status = self.client.login(email='test@example.com', password='test')
        self.assertTrue(login_status)

    def test_logout(self):
        response = self.client.get(reverse('accounts:logout'))
        self.assertEquals(response.status_code, 302)



          