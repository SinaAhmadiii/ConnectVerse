from django.test import TestCase
from users.models import User
from post.models import Post
from comment.models import Comment

class CommentTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@example.com'
        )

        self.post = Post.objects.create(
            user=self.user,
            post_text='Test post'
        )

        self.comment = Comment.objects.create(
            user=self.user,
            post=self.post,
            comment_text='Test comment'
        )

    def test_get_comment_id(self):
        comment_id = self.comment.get_comment_id()
        self.assertEqual(comment_id, self.comment.comment_id)

    def test_get_user(self):
        user = self.comment.get_user()
        self.assertEqual(user, self.user)

    def test_get_post(self):
        post = self.comment.get_post()
        self.assertEqual(post, self.post)

    def test_get_comment_text(self):
        comment_text = self.comment.get_comment_text()
        self.assertEqual(comment_text, self.comment.comment_text)

    def test_str(self):
        expected_str = f"Comment {self.comment.comment_id} by {self.user.username} on Post {self.post.post_id}"
        self.assertEqual(str(self.comment), expected_str)
