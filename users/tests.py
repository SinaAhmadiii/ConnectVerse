from django.test import TestCase
from .models import User

class UserTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'age': 25,
            'phone_number': '1234567890',
            'password': 'password123'
        }

    def test_full_name(self):
        user = User(**self.user_data)
        full_name = user.full_name()
        expected_full_name = 'John Doe'
        self.assertEqual(full_name, expected_full_name)

    def test_set_password(self):
        user = User(**self.user_data)
        new_password = 'newpassword456'
        user.set_password(new_password)
        self.assertEqual(user.password, new_password)

    def test_get_user_by_email_exists(self):
        user = User(**self.user_data)
        user.save()
        retrieved_user = User.get_user_by_email('johndoe@example.com')
        self.assertEqual(retrieved_user, user)

    def test_get_user_by_email_does_not_exist(self):
        retrieved_user = User.get_user_by_email('nonexistent@example.com')
        self.assertIsNone(retrieved_user)
