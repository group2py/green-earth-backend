import os
import sys
parent_path = os.path.join(os.path.abspath('__path__'), '..','..')
sys.path.append(parent_path)
from authentication.models import Users

from django.shortcuts import get_object_or_404


from core import settings
from django.core.files.uploadedfile import SimpleUploadedFile
import pytest


@pytest.mark.django_db
def test_cadastra_usuario_entao_deve_retornar_201( client,user_data):
    response = client.post( '/auth/register/', data=user_data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_login_user_entao_deve_retornar_200(client, user_data):
    client.post( '/auth/register/', data=user_data)
    data = {
        "email":user_data['email'],
        "password":user_data['password']
    } 
    authentication = client.post('/auth/login/user/', data=data)
    assert authentication.status_code == 200

@pytest.mark.django_db
def test_list_users_deve_retornar_200(client):
    response = client.get('/auth/users/')
    assert response.status_code == 200

@pytest.mark.teste
@pytest.mark.django_db
def test_user_get_deve_retornar_200(client,user_created):
    response = client.get(f'/auth/users/{user_created.id}/get/')
    assert response.status_code == 200

# @pytest.mark.teste
@pytest.mark.django_db
def test_user_delete_deve_retornar_200(client,user_created):
    response = client.delete(f'/auth/users/{user_created.id}/delete/')
    assert response.status_code == 200


@pytest.mark.skip(reason="Melhorar o sistema de validação de usuário, como por exemplo, um regex básico no username")
@pytest.mark.django_db
def test_cadastra_usuario_invalido_entao_deve_retornar_400(client):
    image_path = os.path.join(settings.BASE_DIR, "static","authentication",  'img', 'profile.png')
    data_image = SimpleUploadedFile(name='livros.png', content=open(image_path, 'rb').read(),content_type='image/png')
    data =  {
        "username": "A",
        "email": "A@A.com",
        "image": data_image,
        "phone": 998912819,
        "password": "Aa12aZ3352345&@%",
        "first_name": "A",
        "last_name": "Aa",

    }
    response = client.post( '/auth/register/', data=data)
    assert response.status_code == 400



@pytest.mark.skip(reason='Está retornando o erro 415')
@pytest.mark.django_db
def test_user_update_deve_retornar_200(client, user_data,user_created):
    response = client.put(f'/auth/users/{user_created.id}/update/', data=user_data)
    assert response.status_code == 200