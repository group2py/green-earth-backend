#adding path to parent directory
import os
import sys
parent_path = os.path.join(os.path.abspath('__path__'), '..','..')
sys.path.append(parent_path)
from authentication.models import Users


#faker
from faker import Faker
faker = Faker()
#factory
from factory import Factory

#client
from django.test import Client
client = Client()
from django.shortcuts import get_object_or_404

#image
from django.core.files.uploadedfile import SimpleUploadedFile
from core import settings
image_path = os.path.join(settings.BASE_DIR,  "static" , "authentication" ,  'img', 'profile.png')
data_image = SimpleUploadedFile(name='livros.png', content=open(image_path, 'rb').read(),content_type='image/png')


class UserModel:
    def __init__(self,username,email,image,phone,password,gender,first_name,
                 last_name,recovery_email):
        self.username=username
        self.email=email
        self.image=image
        self.phone=phone
        self.password=password
        self.gender=gender
        self.first_name=first_name
        self.last_name=last_name
        self.recovery_email=recovery_email

def user_data_serializer(user_data:UserModel):
    data = {
        "username":user_data.username,
        "email":user_data.email,
        "image":user_data.image,
        "phone":user_data.phone,
        "password":user_data.password,
        "gender":user_data.gender,
        "first_name":user_data.first_name,
        "last_name":user_data.last_name,
        "recovery_email":user_data.recovery_email
}
    return data
class UserFactory(Factory):
    class Meta:
        model = UserModel
    username = faker.name(),
    email = faker.email(),
    image = data_image,
    phone = 9989122819,
    password =  "Aa12aZ3352345&@%" ,
    gender =  "M" ,
    first_name =faker.name(),
    last_name =faker.name(),
    recovery_email = faker.email()

def register_user_in_the_database():
    data = UserFactory.create()
    data = data.__dict__
    client.post("/auth/register/", data=data)
    user = get_object_or_404(Users, email=data['email'][0])
    return user

def register_users_in_the_database(number_of_registrations:int):
    data = UserFactory.create_batch(number_of_registrations)
    database_list = []
    for i in range(len(data)):
        data[i] = data[i].__dict__
        client.post("/auth/register/", data=data[i])
        print(data[i]['email'])
        user = get_object_or_404(Users, email=data[i]['email'][0])
        database_list.append(user)
    return database_list