import pytest
#adding path to parent directory
import os
import sys
parent_path = os.path.join(os.path.abspath('__path__'), '..','..')
sys.path.append(parent_path)

from authentication.models import Users
#faker
from faker import Faker

#image
from django.core.files.uploadedfile import SimpleUploadedFile
from core import settings
#selenium
from time import sleep
from selenium.webdriver import Chrome
    # from selenium.webdriver.common.by import By

#django
from django.shortcuts import get_object_or_404
from django.test import Client
#authentication_factory
from authentication_factory import UserFactory, register_user_in_the_database

@pytest.fixture
def user_data():
    # faker = Faker('pt_BR')
    # image_path = os.path.join(settings.BASE_DIR, "static","authentication",  'img', 'profile.png')
    # data_image = SimpleUploadedFile(name='livros.png', content=open(image_path, 'rb').read(),content_type='image/png')

    # data =  {
    #     "username": faker.name(),
    #     "email": faker.email(),
    #     "image":data_image,
    #     "phone": 9989122819,
    #     "password": "Aa12aZ3352345&@%",
    #     "gender": "M",
    #     "first_name":faker.name(),
    #     "last_name":faker.name(),
    #     "recovery_email": faker.email()
    # }
    data = UserFactory.create()

    return data.__dict__


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

@pytest.fixture
def user_created():
    # client.post("/auth/register/", data=user_data)
    # user = get_object_or_404(Users, email=user_data['email'][0])

    list_users = register_user_in_the_database()
    return list_users