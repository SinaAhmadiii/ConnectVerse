from django.test import TestCase
from users.models import User
from post.models import Post
from comment.models import Comment
from .models import Bookmark

class BookmarkTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')

        self.post = Post.objects.create(user=self.user, post_text='Test post')

        self.comment = Comment.objects.create(user=self.user, post=self.post, comment_text='Test comment')

    def test_bookmark_post(self):
        bookmark = Bookmark.objects.create(user=self.user, post=self.post)
        self.assertEqual(bookmark.user, self.user)
        self.assertEqual(bookmark.post, self.post)

    def test_get_user_bookmarks(self):
        bookmark = Bookmark.objects.create(user=self.user, post=self.post)
        user_bookmarks = Bookmark.objects.filter(user=self.user)
        self.assertIn(bookmark, user_bookmarks)

    def test_get_bookmarked_posts(self):
        bookmark = Bookmark.objects.create(user=self.user, post=self.post)
        bookmarked_posts = Post.objects.filter(bookmark__user=self.user)
        self.assertIn(self.post, bookmarked_posts)

    def test_str_representation(self):
        bookmark = Bookmark.objects.create(user=self.user, post=self.post)
        self.assertEqual(str(bookmark), f"Bookmark ID: {bookmark.bookmark_id}")

    def tearDown(self):
        Bookmark.objects.all().delete()
        Comment.objects.all().delete()
        Post.objects.all().delete()
        User.objects.all().delete()
