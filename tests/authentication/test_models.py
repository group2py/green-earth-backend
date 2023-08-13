import sys
import os
#adding path to parent directory
# parent_path = os.path.join(os.path.abspath('__path__'), '..','..')
# sys.path.append(parent_path)

from core import settings
from django.core.files.uploadedfile import SimpleUploadedFile


from django.test import Client
import pytest
from model_bakery import baker

@pytest.mark.django_db
def test_cadastra_usuario_entao_usuario_deve_estar_cadastrado():
    client = Client()    
    image_path = os.path.join(settings.BASE_DIR, "static","authentication",  'img', 'profile.png')
    data_image = SimpleUploadedFile(name='livros.png', content=open(image_path, 'rb').read(),content_type='image/png')
    data =  {
        "username": "A",
        "email": "A@A.COM",
        "image": data_image,
        "phone": 998912819,
        "password": "Aa12aZ3352345&@%",
        "is_superuser": False,
        "first_name": "A",
        "last_name": "Aa",
        "is_staff": False,
        "is_active": True,
    }
    # data = baker.make("authentication.Users")
    data['password'] = "Aa12aZ3352345&@%"
    # data
    user = client.post('/auth/register/', data=data)
    print(user.json())
    database_client = client.get('/auth/users/1/get/')
    # print(database_client.json()['id'])
    assert database_client.json()['id']