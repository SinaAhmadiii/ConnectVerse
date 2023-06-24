from django.test import TestCase
from users.models import User
from post.models import Post
from .models import Bookmark

class BookmarkModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='testuser')
        cls.post = Post.objects.create(title='Test Post', content='This is a test post.')

    def test_bookmark_creation(self):
        bookmark = Bookmark.objects.create(user=self.user, post=self.post)

        self.assertTrue(isinstance(bookmark, Bookmark))
        self.assertEqual(bookmark.user, self.user)
        self.assertEqual(bookmark.post, self.post)

    def test_get_user_bookmarks(self):
        Bookmark.objects.create(user=self.user, post=self.post)
        Bookmark.objects.create(user=self.user, post=self.post)

        bookmarks = Bookmark.objects.get_user_bookmarks(self.user)

        self.assertEqual(len(bookmarks), 2)
        for bookmark in bookmarks:
            self.assertEqual(bookmark.user, self.user)

    def test_get_bookmarked_posts(self):
        Bookmark.objects.create(user=self.user, post=self.post)
        Bookmark.objects.create(user=self.user, post=self.post)

        bookmarks = Bookmark.objects.get_bookmarked_posts(self.user)

        self.assertEqual(len(bookmarks), 2)
        for bookmark in bookmarks:
            self.assertEqual(bookmark.post, self.post)
