from django.test import TestCase, Client
from django.contrib.auth import get_user, get_user_model

class GoogleLoginTest(TestCase):

    # Create a user for testing
    # Custom user model references adapted from https://docs.djangoproject.com/en/3.2/topics/auth/customizing/
    @classmethod
    def setUp(cls):
        user_model = get_user_model()
        cls.test_user = user_model.objects.create(email='test@example.com')
        cls.test_user.set_password('Abcdefg1!')
        cls.test_user.save()
    
    # Test login credentials
    # User auth attributes found in https://docs.djangoproject.com/en/3.2/ref/contrib/auth/
    # Client login code adapted from https://docs.djangoproject.com/en/3.2/topics/testing/tools/
    def test_login(self):
        c = Client()
        c.login(email='test@example.com', password='Abcdefg1!')
        user = get_user(c)
        self.assertTrue(user.is_authenticated)
    
    # Test logging out
    def test_logout(self):
        c = Client()
        c.force_login(self.test_user)
        self.assertTrue(get_user(c).is_authenticated)
        
        c.logout()
        self.assertFalse(get_user(c).is_authenticated)
    
    # Test incorrect email
    def test_wrong_email(self):
        c = Client()
        c.login(email='example@test.com', password='Abcdefg1!')
        self.assertFalse(get_user(c).is_authenticated)
    
    # Test incorrect password
    def test_wrong_password(self):
        c = Client()
        c.login(email='test@example.com', password='abcdefg1!')
        self.assertFalse(get_user(c).is_authenticated)