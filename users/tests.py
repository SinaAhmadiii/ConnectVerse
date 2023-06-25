from django.test import TestCase
from users.models import User

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='test@example.com',
            first_name='John',
            last_name='Doe',
            age=25,
            phone_number='1234567890'
        )

    def test_full_name(self):
        full_name = self.user.full_name()
        self.assertEqual(full_name, 'John Doe')

    def test_set_password(self):
        new_password = 'newpassword'
        self.user.set_password(new_password)
        self.assertTrue(self.user.check_password(new_password))

    def test_get_user_by_email(self):
        user = User.get_user_by_email('test@example.com')
        self.assertEqual(user, self.user)

    def test_get_user_by_nonexistent_email(self):
        user = User.get_user_by_email('nonexistent@example.com')
        self.assertIsNone(user)

    def test_str_representation(self):
        user_str = str(self.user)
        self.assertEqual(user_str, 'testuser')

    def tearDown(self):
        self.user.delete()
