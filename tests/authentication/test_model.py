import requests
import json
import os
from core import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client
import pytest
@pytest.mark.django_db
def test_cadastra_usuario_entao_deve_retornar_201():
    c = Client()    
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

    # Enviando a requisição com a imagem
    response = c.post( '/auth/register/', data=data)

    assert response.status_code == 201
    
