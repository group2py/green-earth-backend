import sys
import os
#adding path to parent directory
parent_path = os.path.join(os.path.abspath('__path__'), '..','..')
sys.path.append(parent_path)

from core import settings
from django.core.files.uploadedfile import SimpleUploadedFile


from django.test import Client
import pytest

from authentication.models import Users


@pytest.mark.django_db
def test_register_user_then_user_must_be_registered(client,user_data):
    client.post('/auth/register/', data=user_data)
    database_client = Users.objects.filter(email=user_data['email'])
    assert database_client