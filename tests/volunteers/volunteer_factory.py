import os
import sys
parent_path = os.path.join(os.path.abspath('__path__'), '..','..')
sys.path.append(parent_path)

# User Factory
from tests.authentication.authentication_factory import register_user_in_the_database
#Factory Boy
from factory import Factory


# faker
from faker import Faker
faker = Faker()

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
class VolunteerFactory(Factory):
    class Meta:
        model=VolunteerModel
    user = register_user_in_the_database()
    help = faker.text() 
    created = faker.date_time()