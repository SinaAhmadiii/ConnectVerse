from django.test import TestCase
from users.models import User
from models import Post

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for the test
        user = User.objects.create(username='testuser')
        
        # Create a post for the test
        Post.objects.create(user=user, post_text='Test post')

    def test_post_str_representation(self):
        post = Post.objects.get(post_id=1)
        expected_str = "Post 1 by testuser"
        self.assertEqual(str(post), expected_str)

    def test_increment_likes(self):
        post = Post.objects.get(post_id=1)
        initial_likes = post.likes_count
        post.increment_likes()
        updated_likes = post.likes_count
        self.assertEqual(updated_likes, initial_likes + 1)

    def test_verbose_names(self):
        post = Post.objects.get(post_id=1)
        field_names = {
            'post_id': 'Post ID',
            'user': 'User',
            'post_text': 'Post Text',
            'likes_count': 'Likes Count',
            'views_count': 'Views Count',
        }
        for field in post._meta.fields:
            self.assertEqual(field.verbose_name, field_names[field.name])
