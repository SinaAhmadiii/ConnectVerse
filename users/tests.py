from django.test import Client
import pytest

@pytest.mark.django_db
def test_register_view():
    client = Client()
    response = client.post('/users/register/', {
        'first_name': 'John',
        'last_name': 'Doe',
        'username': 'johndoe',
        'email': 'johndoe@example.com',
        'age': 25,
        'phone_number': '1234567890',
        'password': 'password123',
    })
    assert response.status_code == 302  
    assert response.url == '/users/login/'  

@pytest.mark.django_db
def test_login_view():
    client = Client()
    response = client.post('/users/login/', {
        'email': 'johndoe@example.com',
        'password': 'password123',
    })
    assert response.status_code == 302  
    assert response.url == '/home/'  
    
