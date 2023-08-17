#pytest
import pytest
#django
from django.test import Client
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
#model_bakery
from model_bakery import baker
# #models
import os
import sys
from faker import Faker
parent_path = os.path.join(os.path.abspath('__path__'), '..','..')
sys.path.append(parent_path)
from contributors.models import Contributors
from tests.authentication.conftest import user_created,user_data
from authentication.models import Users
import json
#image
from django.core.files.uploadedfile import SimpleUploadedFile
from core import settings
@pytest.fixture
def contributors_data(client, user_created):
    faker = Faker('pt_BR')
    user_data = model_to_dict(user_created)
    image_path = os.path.join(settings.BASE_DIR, "static","authentication",  'img', 'profile.png')
    data_image = SimpleUploadedFile(name='livros.png', content=open(image_path, 'rb').read(),content_type='image/png')
    user_data['image'] = data_image
    user_data['last_login'] = faker.date_time()
    client.post('/auth/register/', data=user_data)
    user = get_object_or_404(Users, email=user_data['email'])
  
    data = {
        "user":user.id,
        "company":'hahaha',
        "description": 'hahahaa',
        "role": 'hahahaa'
    }
    return data


@pytest.fixture
def contributors_created(client, contributors_data):
    client.post('/contributors/create_contributors/', data=contributors_data)
    print(contributors_data['user'])
    contributor = get_object_or_404(Contributors, user=contributors_data['user']
                                     )

  
    return contributor


@pytest.fixture
def contributors_history_data(client,user_created):
    faker = Faker('pt_BR')
    user_data = model_to_dict(user_created)
    image_path = os.path.join(settings.BASE_DIR, "static","authentication",  'img', 'profile.png')
    data_image = SimpleUploadedFile(name='livros.png', content=open(image_path, 'rb').read(),content_type='image/png')
    user_data['image'] = data_image
    user_data['last_login'] = faker.date_time()
    client.post('/auth/register/', data=user_data)
    user = get_object_or_404(Users, email=user_data['email'])

    data ={
        "user": user.id,
        "company": "hahaha",
        "value": "hahaha",
        "created": "hahaha"
    }
    return data
@pytest.fixture
def contributors_history_created(client,contributors_history_data):
    client.post('create_contributors_history/', data=contributors_history_data)
   
    contributor_history = get_object_or_404(Contributors, user=['user']
                                     )
   
  
    return contributor_history