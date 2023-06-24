from django.test import TestCase
from users.models import User
from post.models import Post
from comment.models import Comment

class CommentModelTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create(username='testuser')

        # Create a post
        self.post = Post.objects.create(title='Test Post', content='This is a test post.')

        # Create a comment
        self.comment = Comment.objects.create(user=self.user, post=self.post, comment_text='This is a test comment.')

    def test_comment_id(self):
        self.assertEqual(self.comment.get_comment_id(), self.comment.comment_id)

    def test_user(self):
        self.assertEqual(self.comment.get_user(), self.user)

    def test_post(self):
        self.assertEqual(self.comment.get_post(), self.post)

    def test_comment_text(self):
        self.assertEqual(self.comment.get_comment_text(), 'This is a test comment.')

    def test_string_representation(self):
        expected_string = f"Comment {self.comment.comment_id} by {self.user.username} on Post {self.post.post_id}"
        self.assertEqual(str(self.comment), expected_string)
