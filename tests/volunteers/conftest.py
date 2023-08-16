import pytest
#adding path to parent directory
import os
import sys
parent_path = os.path.join(os.path.abspath('__path__'),'..', '..')
sys.path.append(parent_path)

from authentication.models import Users
#faker
from faker import Faker
#selenium
from time import sleep
from selenium.webdriver import Chrome
    # from selenium.webdriver.common.by import By
from tests.authentication.authentication_factory import register_user_in_the_database

#django
from django.shortcuts import get_object_or_404
from django.test import Client
#authentication_factory
from tests.volunteers.volunteer_factory import register_volunteer_in_database, VolunteerFactory
# from tests.volunteers.volunteer_factory import register_volunteer_in_database

@pytest.fixture
@pytest.mark.django_db
def volunteer_data():
    faker = Faker()
    data = {'user ': register_user_in_the_database(),
            'help ': faker.text(),
            'created ': faker.date_time()}
   
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
def volunteer_created():
    # client.post("/auth/register/", data=volunteer_data)
    # volunteer = get_object_or_404(Users, email=volunteer_data['email'][0])
    volunteer = register_volunteer_in_database()
    return volunteer
