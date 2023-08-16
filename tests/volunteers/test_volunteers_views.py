import pytest
#django
from django.shortcuts import get_object_or_404
#adding path to parent directory
import os
import sys
parent_path = os.path.join(os.path.abspath('__path__'), '..','..')
sys.path.append(parent_path)
from volunteers.models import Volunteers

@pytest.mark.skip(reason="a")
@pytest.mark.django_db
def test_list_volunteers_then_must_return_200(client):
    response = client.get('/volunteers/list/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_creates_volunteers_then_returns_201(client, volunteer_data):
    response = client.post('/volunteers/create/', data=volunteer_data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_get_volunteer_then_must_return_200(client, volunteer_created):

    volunteer = get_object_or_404(Volunteers, id=volunteer_created.id)
    response = client.get(f'/volunteers/{volunteer.id}/get/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_delete_volunteer_must_return_200(client, volunteer_created):
    volunteer = get_object_or_404(Volunteers, id=volunteer_created.id)
    response = client.get(f'/volunteers/{volunteer.id}/delete/')
    assert response.status_code == 200



    #'<int:pk>/delete/'