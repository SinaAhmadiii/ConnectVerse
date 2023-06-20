from django.test import RequestFactory
from django.urls import reverse
import pytest
from .models import Comment
from .views import comment_detail

@pytest.mark.django_db
def test_comment_detail_view():
    comment = Comment.objects.create(comment_id=1, user_id=1, post_id=1, comment_text='Test comment')
    request = RequestFactory().get(reverse('comment:comment_detail', args=[comment.comment_id]))
    response = comment_detail(request, comment_id=comment.comment_id)
    assert response.status_code == 200
    assert 'comment' in response.context
    assert 'comment/comment_detail.html' in response.template_name
