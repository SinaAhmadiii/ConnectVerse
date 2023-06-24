from django.db import models
from users.models import User
from comment.models import Comment

class Reply(models.Model):
    reply_id = models.AutoField(primary_key=True, verbose_name='Reply ID')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name='Comment')
    reply_text = models.TextField(verbose_name='Reply Text', help_text='Enter your reply here.')

    def __str__(self):
        return f"Reply {self.reply_id} by {self.user.username} on Comment {self.comment.comment_id}"

    def get_user(self):
        return self.user

    def get_comment(self):
        return self.comment

    def get_reply_text(self):
        return self.reply_text

    def update_reply_text(self, new_text):
        self.reply_text = new_text
        self.save()

    def delete_reply(self):
        self.delete()

    def get_total_likes(self):
        return self.reply_likes.count()

    def get_liked_users(self):
        return [like.user for like in self.reply_likes.all()]
