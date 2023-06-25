from django.test import TestCase
from users.models import User
from post.models import Post

class PostTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create(username='testuser')

        # Create a post for testing
        self.post = Post.objects.create(user=self.user, post_text='Test post')

    def test_increment_likes(self):
        initial_likes_count = self.post.likes_count
        self.post.increment_likes()
        updated_post = Post.objects.get(post_id=self.post.post_id)
        self.assertEqual(updated_post.likes_count, initial_likes_count + 1)

    def test_str_representation(self):
        expected_str = f"Post {self.post.post_id} by {self.user.username}"
        self.assertEqual(str(self.post), expected_str)
