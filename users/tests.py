from django.test import TestCase
from .models import User

class UserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name="John",
            last_name="Doe",
            username="johndoe",
            email="johndoe@example.com",
            age=25,
            phone_number="1234567890",
        )

    def test_full_name(self):
        full_name = self.user.full_name()
        self.assertEqual(full_name, "John Doe")

    def test_set_password(self):
        new_password = "newpassword"
        self.user.set_password(new_password)
        self.assertTrue(self.user.check_password(new_password))

    def test_get_user_by_email(self):
        email = "johndoe@example.com"
        user = User.get_user_by_email(email)
        self.assertEqual(user, self.user)

    def test_string_representation(self):
        string_representation = str(self.user)
        self.assertEqual(string_representation, "johndoe")
