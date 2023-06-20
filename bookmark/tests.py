import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Bookmark
from .views import bookmark_list, bookmark_detail, bookmark_post, remove_bookmark


@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='testpassword')


@pytest.fixture
def bookmark(user):
    return Bookmark.objects.create(user=user, post_id=1)


@pytest.mark.django_db
def test_bookmark_list(client, user):
    Bookmark.objects.create(user=user, post_id=1)
    Bookmark.objects.create(user=user, post_id=2)

    url = reverse('bookmark:bookmark_list')
    response = client.get(url)

    assert response.status_code == 200
    assert 'Bookmark List' in response.content.decode()
    assert 'Bookmark ID: 1' in response.content.decode()
    assert 'Bookmark ID: 2' in response.content.decode()


@pytest.mark.django_db
def test_bookmark_detail(client, user, bookmark):
    url = reverse('bookmark:bookmark_detail', kwargs={'bookmark_id': bookmark.id})
    response = client.get(url)

    assert response.status_code == 200
    assert f'Bookmark ID: {bookmark.id}' in response.content.decode()
    assert f'User: {user}' in response.content.decode()
    assert f'Post ID: {bookmark.post_id}' in response.content.decode()


@pytest.mark.django_db
def test_bookmark_post(client, user):
    url = reverse('bookmark:bookmark_post', kwargs={'post_id': 1})
    response = client.get(url)

    assert response.status_code == 200
    assert 'Bookmark Post' in response.content.decode()
    assert 'Bookmark added successfully!' in response.content.decode()


@pytest.mark.django_db
def test_remove_bookmark(client, user, bookmark):
    url = reverse('bookmark:remove_bookmark', kwargs={'bookmark_id': bookmark.id})
    response = client.get(url)

    assert response.status_code == 200
    assert 'Remove Bookmark' in response.content.decode()
    assert 'Bookmark removed successfully!' in response.content.decode()
