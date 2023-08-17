import pytest
# adding path to parent directory
import os
import sys

parent_path = os.path.join(os.path.abspath('__path__'), '..', '..')
sys.path.append(parent_path)
from tests.conftest import user_created

from authentication.models import Users
from django.test import Client
import json
from faker import Faker

from core import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from django.shortcuts import get_object_or_404


@pytest.fixture
def browser():
    browser = Chrome()
    url = "https://courageous-jalebi-621420.netlify.app/"
    browser.get(url)

    sleep(2)
    return browser


# @pytest.fixture
# def user_data():
#     faker = Faker()
#     image_path = os.path.join(settings.BASE_DIR, "static","authentication",  'img', 'profile.png')
#     data_image = SimpleUploadedFile(name='livros.png', content=open(image_path, 'rb').read(),content_type='image/png')

#     data =  {
#         "username": faker.name(),
#         "email": faker.email(),
#         "image":data_image,
#         "phone": 9989122819,
#         "password": "Aa12aZ3352345&@%",
#         "gender": "M",
#         "first_name":faker.name(),
#         "last_name":faker.name(),
#         "recovery_email": faker.email()
#     }
#     return data

@pytest.fixture
@pytest.fixture
def client():
    client = Client()
    return client


# @pytest.fixture
# def user_created(client, user_data):
#     client.post( '/auth/register/', data=user_data)
#     client_created = get_object_or_404(Users, email=user_data['email'])
#     print(client_created.id)
#     return client_created

def post_data(user_created):
    faker = Faker()
    data = {
        "owner": user_created,
        "title": faker.text(),
        "description": faker.text(),
        "state": faker.state(),
        "city": faker.city(),
    }
    # .strftime('%d_%m_%Y %H:%M')
