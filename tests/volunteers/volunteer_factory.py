#adding path to parent directory
import os
import sys
parent_path = os.path.join(os.path.abspath('__path__'), '..','..')
sys.path.append(parent_path)
from volunteers.models import Volunteers

# User Factory
from tests.authentication.authentication_factory import register_user_in_the_database
#Factory Boy
from factory import Factory
# faker
from faker import Faker
faker = Faker()

#client
from django.test import Client
client = Client()

#django
from django.shortcuts import get_object_or_404

#pytest
import pytest

class VolunteerModel():
    """Class that generates multiple volunteers with multiple missions
    
    structure: {user:Users, help:str, created:<date_time>}
    """

    def __init__(self,user,help,created):
        self.user = user 
        self.help = help 
        self.created = created 

def volunteer_data_serializer(volunter:VolunteerModel):
    data = { "user": volunter.user,
            "help": volunter.help,
            "created": volunter.created}
    return data
@pytest.mark.django_db
class VolunteerFactory(Factory):
    class Meta:
        model=VolunteerModel

    user = register_user_in_the_database()
    help = faker.text() 
    created = faker.date_time()

@pytest.mark.django_db
def register_volunteer_in_database():
    data = VolunteerFactory.create()
    data = data.__dict__
    client.post("/volunteers/create/", data=data)
    volunteer = get_object_or_404(Volunteers, email=data['email'][0])
    return volunteer