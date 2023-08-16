# IMPORTS LIBRARIES PYTHON
import os
import sys
import pytest
from core import settings

# IMPORTS FILES
from blog.models import *

# IMPORT DJANGO
from django.shortcuts import get_object_or_404
from django.core.files.uploadedfile import SimpleUploadedFile

# PATH SYSTEM
parent_path = os.path.join(os.path.abspath('__path__'), '..', '..')
sys.path.append(parent_path)

@pytest.mark.django_db
def test_list_post_blog_ong_return_200(client):
    response = client.get('/blog/post/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_register_post_ong_return_201(client, user_data):
    response = client.post('/blog/create_post/', data=user_data)
    assert response.status_code == 201

@pytest.mark.django_db
def test_get_post_ong_return_200(client, user_data):
    client.post('/blog/create_post/', data=user_data)
    response = client.get('/blog/post/1/get/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_delete_post_ong_return_200(client, user_data):
    client.post('/blog/post/<int:pk>/delete/', data=user_data)
    user_id = get_object_or_404(BlogPost, pk=user_data['id']).id
    response = client.delete(f'/blog/post/{user_id}/delete/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_update_post_ong_return_200(client, user_data):
    client.post('/blog/create_post/', data=user_data)
    post = get_object_or_404(BlogPost, pk=user_data['id']).id
    response = client.put(f'/blog/post/{post}/update/')
    assert response.status_code == 200