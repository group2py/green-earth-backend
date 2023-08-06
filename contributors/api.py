# LIBRARIES PYTHON
from typing import Any

# DJANGO REST FRAMEWORK IMPORTS
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# DJANGO
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# FILES APPS IMPORTS
from .models import Contributors, ContributionHistory
from .serializers import ContributorsModelsSerializer, ContributionHistoryModelsSerializer
from .utils import validate_fields

class CreateContributors(ModelViewSet):
    queryset = Contributors.objects.all()
    serializer_class = ContributorsModelsSerializer

    def list(self, request: HttpResponse):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request: HttpResponse):
        queryset = self.filter_queryset(self.get_queryset())
        data = request.data

        if not validate_fields(data['company'], data['description']):
            return Response({'error': 'Fields invalids'}, status=status.HTTP_400_BAD_REQUEST)

        serializers = self.get_serializer(data=data)
        serializers.is_valid(raise_exception=True)
        create_contributors = serializers.save()
        return Response({'success': 'Partnership made successfully. Thanks for your donation!'}, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request: HttpResponse, pk):
        contributors = get_object_or_404(Contributors, pk=pk)

        if isinstance(contributors, Contributors):
            response = {
                'user': contributors.user,
                'company': contributors.company,
                'description': contributors.description,
                'role': contributors.role,
            }
            serializer = self.get_serializer(response)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'User does not instance of Contributors'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request: HttpResponse, pk):
        contributors = get_object_or_404(Contributors, pk=pk)

        if isinstance(contributors, Contributors):
            contributors.delete()
            return Response({'success': 'Contributors deleted successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'contributors does not instance of Contributors'}, status=status.HTTP_400_BAD_REQUEST)

class CreateContributionHistory(ModelViewSet):
    queryset = ContributionHistory.objects.all()
    serializer_class = ContributionHistoryModelsSerializer

    def list(self, request: HttpResponse, *args: Any, **kwargs: Any):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request: HttpResponse, *args: Any, **kwargs: Any):
        queryset = self.filter_queryset(self.get_queryset())
        data = request.data

        if not validate_fields(data['company'], data['value']):
            return Response({'error': 'Fields invalids'}, status=status.HTTP_400_BAD_REQUEST)

        serializers = self.get_serializer(data=data)
        serializers.is_valid(raise_exception=True)
        create_contributors_history = serializers.save()
        return Response({'success': 'Contribution made successfully!'}, status=status.HTTP_201_CREATED)
