from django.test import TestCase
from users.models import User
from comment.models import Comment
from .models import Reply

class ReplyModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='testuser')
        comment = Comment.objects.create(comment_id=1, text='Test comment')
        Reply.objects.create(user=user, comment=comment, reply_text='Test reply')

    def test_get_user(self):
        reply = Reply.objects.get(reply_id=1)
        user = reply.get_user()
        self.assertEqual(user.username, 'testuser')

    def test_get_comment(self):
        reply = Reply.objects.get(reply_id=1)
        comment = reply.get_comment()
        self.assertEqual(comment.text, 'Test comment')

    def test_get_reply_text(self):
        reply = Reply.objects.get(reply_id=1)
        reply_text = reply.get_reply_text()
        self.assertEqual(reply_text, 'Test reply')

    def test_update_reply_text(self):
        reply = Reply.objects.get(reply_id=1)
        reply.update_reply_text('Updated reply')
        updated_reply = Reply.objects.get(reply_id=1)
        self.assertEqual(updated_reply.reply_text, 'Updated reply')

    def test_delete_reply(self):
        reply = Reply.objects.get(reply_id=1)
        reply.delete_reply()
        remaining_replies = Reply.objects.count()
        self.assertEqual(remaining_replies, 0)

    def test_get_total_likes(self):
        reply = Reply.objects.get(reply_id=1)
        self.assertEqual(reply.get_total_likes(), 0)

    def test_get_liked_users(self):
        reply = Reply.objects.get(reply_id=1)
        self.assertQuerysetEqual(reply.get_liked_users(), [])
