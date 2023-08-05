# LIBRARIES PYTHON
from typing import Any

# DJANGO REST FRAMEWORK IMPORTS
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# DJANGO
from django.http import HttpResponse

# FILES APPS IMPORTS
from .models import CrimeDenunciations, MediaOng, BlogPost
from .serializers import CrimeDenunciationsModelsSerializer, MediaOngModelsSerializer, BlogPostModelsSerializer
from .utils import validate_fields


class CreateCrimeDenunciations(ModelViewSet):
    queryset = CrimeDenunciations.objects.all()
    serializer_class = CrimeDenunciationsModelsSerializer

    def list(self, request: HttpResponse, *args: Any, **kwargs: Any):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request: HttpResponse, *args: Any, **kwargs: Any):
        queryset = self.filter_queryset(self.get_serializer())

        data = request.data
        
        if not validate_fields(data['user'], data['description'], data['state'], data['city'], data['address'], data['number'], data['reference_point']):
            return Response({'error': 'fields invalids'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        create_crime_denunciations = serializer.save()

        return Response({'success': 'Reported successfully!'}, status=status.HTTP_201_CREATED)