# LIBRARIES PYTHON
from typing import Any

# DJANGO REST FRAMEWORK IMPORTS
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# DJANGO
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# FILES APPS IMPORTS
from .models import Volunteers
from .utils import validate_fields
from .serializers import VolunteersModelsSerializers


# LIST OBJECTS
class ListVolunteers(APIView):
    def get(self, request: HttpResponse):
        contributors = Volunteers.objects.all()
        serializer = VolunteersModelsSerializers(contributors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# CREATE OBJECTS
class CreateVolunteers(APIView):
    def post(self, request: HttpResponse):
        queryset = self.filter_queryset(self.get_queryset())
        data = request.data

        if not validate_fields(data['help']):
            return Response({'error': 'Fields invalids'}, status=status.HTTP_400_BAD_REQUEST)

        serializers = VolunteersModelsSerializers(data=data)
        serializers.is_valid(raise_exception=True)
        create_contributors = serializers.save()
        return Response({'success': 'registered volunteer. Thanks for being a part!'}, status=status.HTTP_201_CREATED)


# PICK UP AN OBJECTS
class GetVolunteers(APIView):
    def get(self, request: HttpResponse, pk):
        volunteers = get_object_or_404(Volunteers, pk=pk)

        if isinstance(volunteers, Volunteers):
            response = {
                    'user': volunteers.user,
                    'help': volunteers.help,
                }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'volunteers is not an instance of Volunteers'})


# DELETE OBJECTS
class DeleteVolunteers(APIView):
    def delete(self, request: HttpResponse, pk):
        volunteers = get_object_or_404(Volunteers, pk=pk)

        if isinstance(volunteers, Volunteers):
            volunteers.delete()
            return Response({'success': 'volunteers deleted successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'volunteers does not instance of Volunteers'}, status=status.HTTP_400_BAD_REQUEST)