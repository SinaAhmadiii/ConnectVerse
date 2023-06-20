from django.db import models
from users.models import User
from post.models import Post

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField()

    def __str__(self):
        return f"Comment {self.comment_id} by {self.user.username} on Post {self.post.post_id}"
