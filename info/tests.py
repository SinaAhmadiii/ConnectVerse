from django.test import TestCase
from users.models import User
from models import Profile

class ProfileModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com')
        self.profile = Profile.objects.create(user=self.user)

    def test_get_full_name(self):
        full_name = self.profile.get_full_name()
        self.assertEqual(full_name, self.user.get_full_name())

    def test_get_username(self):
        username = self.profile.get_username()
        self.assertEqual(username, self.user.username)

    def test_update_profile_picture(self):
        new_picture = 'path/to/new_picture.jpg'
        self.profile.update_profile_picture(new_picture)
        self.assertEqual(self.profile.profile_picture, new_picture)

    def test_add_bio(self):
        new_bio = 'This is a new bio.'
        self.profile.add_bio(new_bio)
        self.assertEqual(self.profile.bio, new_bio)

    def test_delete_profile(self):
        self.profile.delete_profile()
        self.assertFalse(Profile.objects.filter(user=self.user).exists())
        self.assertFalse(User.objects.filter(username='testuser').exists())
