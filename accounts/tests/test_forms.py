from django.test import TestCase



class UserFormTests(TestCase):

    def test_login_form(self):
        response = self.client.post(
            '/accounts/login/', data={'email':'test@example.com', 'password': 'test0123'}
        )
        self.assertEqual(response.status_code, 200)
    
    def test_signup_form(self):
        response = self.client.post(
            '/accounts/signup/', 
            data={'username':'test_user', 'email':'test@example.com', 'password':'password', 'confirm_password':'confirm_password'}
        )
        self.assertEqual(response.status_code, 200)