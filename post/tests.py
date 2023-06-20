from django.test import RequestFactory
from django.urls import reverse
import pytest
from .models import Post
from .views import post_detail

@pytest.mark.django_db
def test_post_detail_view():
    post = Post.objects.create(post_id=1, user_id=1, post_text='Test post', likes_count=0, views_count=0)
    request = RequestFactory().get(reverse('post:post_detail', args=[post.post_id]))
    response = post_detail(request, post_id=post.post_id)
    assert response.status_code == 200
    assert 'post' in response.context
    assert 'post/post_detail.html' in response.template_name
