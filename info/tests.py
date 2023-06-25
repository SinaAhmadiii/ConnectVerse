from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from users.models import User
from info.models import Profile

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.profile = Profile.objects.create(user=self.user)

    def tearDown(self):
        self.profile.delete()
        self.user.delete()

    def test_get_full_name(self):
        full_name = self.profile.get_full_name()
        expected_name = f"{self.user.first_name} {self.user.last_name}"
        self.assertEqual(full_name, expected_name)

    def test_get_username(self):
        username = self.profile.get_username()
        self.assertEqual(username, self.user.username)

    def test_update_profile_picture(self):
        new_picture = SimpleUploadedFile(
            "new_picture.jpg",
            b"dummy_image_content",
            content_type="image/jpeg"
        )
        self.profile.update_profile_picture(new_picture)
        self.assertEqual(self.profile.profile_picture, new_picture)

    def test_add_bio(self):
        new_bio = "This is my updated bio."
        self.profile.add_bio(new_bio)
        self.assertEqual(self.profile.bio, new_bio)

    def test_delete_profile(self):
        self.profile.delete_profile()
        self.assertFalse(User.objects.filter(username=self.user.username).exists())
        self.assertFalse(Profile.objects.filter(user=self.user).exists())
