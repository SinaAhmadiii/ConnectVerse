from django.test import RequestFactory
from django.urls import reverse
import pytest
from .models import Reply
from .views import reply_detail

@pytest.mark.django_db
def test_reply_detail_view():
    reply = Reply.objects.create(reply_id=1, user_id=1, comment_id=1, reply_text='Test reply')
    request = RequestFactory().get(reverse('reply:reply_detail', args=[reply.reply_id]))
    response = reply_detail(request, reply_id=reply.reply_id)
    assert response.status_code == 200
    assert 'reply' in response.context
    assert 'reply/reply_detail.html' in response.template_name
