import os


from core import settings
from django.core.files.uploadedfile import SimpleUploadedFile
import pytest


@pytest.mark.django_db
def test_cadastra_usuario_entao_deve_retornar_201(user_data, client):
    response = client.post( '/auth/register/', data=user_data)
    assert response.status_code == 201

@pytest.mark.skip(reason="Melhorar o sistema de validação de usuário")
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

