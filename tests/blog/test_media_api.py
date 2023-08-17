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
def test_list_media_ong_return_200(client):
    response = client.get('/blog/media/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_register_media_ong_return_201(client, user_data):
    response = client.post('/blog/create_media/', data=user_data)
    assert response.status_code == 201

@pytest.mark.django_db
def test_get_media_ong_return_200(client, user_data):
    client.post('/blog/create_post/', data=user_data)
    response = client.get('/blog/media/1/get/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_update_media_ong_return_200(client, user_data):
    client.post('/blog/create_media/', data=user_data)
    media = get_object_or_404(MediaOng, pk=user_data['id']).id
    response = client.put(f'/blog/media/{media}/update/')
    assert response.status_code == 200