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
from contributors.models import Contributors, ContributionHistory
from tests.authentication.conftest import user_created,user_data
from authentication.models import Users
from volunteers.models import Volunteers

#image
from django.core.files.uploadedfile import SimpleUploadedFile
from core import settings
#selenium
from time import sleep
from selenium.webdriver import Chrome
    # from selenium.webdriver.common.by import By

@pytest.fixture
@pytest.mark.django_db
def volunteer_data(client,user_created):
    faker = Faker('pt_BR')
    user_data = model_to_dict(user_created)
    image_path = os.path.join(settings.BASE_DIR, "static","authentication",  'img', 'profile.png')
    data_image = SimpleUploadedFile(name='livros.png', content=open(image_path, 'rb').read(),content_type='image/png')
    user_data['image'] = data_image
    user_data['last_login'] = faker.date_time()
    client.post('/auth/register/', data=user_data)
    user = get_object_or_404(Users, email=user_data['email'])
    data = {"choceis":"educacao_ambiental",
            'user': user.id,
            'help': faker.text(),
            'created': faker.date_time()}
   
    return data


@pytest.fixture
def browser():
    browser = Chrome()
    url = "https://courageous-jalebi-621420.netlify.app/"
    browser.get(url)
    sleep(2)
    return browser


@pytest.fixture
def client():
    client = Client()    
    return client

@pytest.mark.django_db
@pytest.fixture
def volunteer_created(client, volunteer_data):
    response = client.post("/volunteers/create/", data=volunteer_data)
    print(response)
    volunteer = Volunteers.objects.filter(user=volunteer_data['user'], help=volunteer_data['help'], created=volunteer_data['created'])
    
    assert volunteer.exists()
    return volunteer
