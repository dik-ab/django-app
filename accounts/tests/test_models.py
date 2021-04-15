from django.test import TestCase
from accounts.models import Users



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
        self.assertEqual(actual_user.email, email)
        self.assertEqual(actual_user.is_active, is_active)
        self.assertEqual(actual_user.is_staff, is_staff)