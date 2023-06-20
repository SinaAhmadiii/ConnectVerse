from django.db import models
from users.models import User
from comment.models import Comment

class Reply(models.Model):
    reply_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reply_text = models.TextField()

    def __str__(self):
        return f"Reply {self.reply_id} by {self.user.username} on Comment {self.comment.comment_id}"
