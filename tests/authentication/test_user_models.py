import sys
import os
#adding path to parent directory
parent_path = os.path.join(os.path.abspath('__path__'), '..','..')
sys.path.append(parent_path)
from authentication.models import Users


from django.shortcuts import get_object_or_404


from django.test import Client
import pytest

@pytest.mark.django_db
def test_register_user_then_user_must_be_registered(user_created):
    database_client = get_object_or_404(Users, id=user_created.id)
    assert database_client