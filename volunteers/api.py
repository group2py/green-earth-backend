# LIBRARIES PYTHON
from typing import Any

# DJANGO REST FRAMEWORK IMPORTS
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# DJANGO
from django.http import HttpResponse

# FILES APPS IMPORTS
from .models import Volunteers
from .serializers import VolunteersModelsSerializers
from .utils import validate_fields


class CreateVolunteers(ModelViewSet):
    # permission_classes = [IsAuthenticated, ]
    queryset = Volunteers.objects.all()
    serializer_class = VolunteersModelsSerializers

    def list(self, request: HttpResponse):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request: HttpResponse):
        queryset = self.filter_queryset(self.get_queryset())
        data = request.data

        if not validate_fields(data['help']):
            return Response({'error': 'field Invalid'}, status=status.HTTP_400_BAD_REQUEST)        

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        create_volunteers = serializer.save()
        return Response({'success': 'Registered successfully'}, status=status.HTTP_201_CREATED)
    