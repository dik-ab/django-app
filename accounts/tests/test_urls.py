from django.test import TestCase
from django.urls import resolve
from accounts.views import UserLoginView, UserLogoutView, SignUpView



class TestAccountsUrls(TestCase):

    def test_user_login_url(self):
        view = resolve('/accounts/login/')
        self.assertEqual(view.func.view_class, UserLoginView)
    
    def test_user_logout_url(self):
        view = resolve('/accounts/logout/')
        self.assertEqual(view.func.view_class, UserLogoutView)

    def test_user_signup_url(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.view_class, SignUpView)
