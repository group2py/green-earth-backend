# LIBRARIES PYTHON
from typing import Any

# DJANGO REST FRAMEWORK IMPORTS
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# DJANGO
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# FILES APPS IMPORTS
from .models import Contributors, ContributionHistory
from .serializers import ContributorsModelsSerializer, ContributionHistoryModelsSerializer
from .utils import validate_fields


# LIST OBJECTS
class ListContributors(APIView):
    def get(self, request: HttpResponse):
        contributors = Contributors.objects.all()
        serializer = ContributorsModelsSerializer(contributors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ListContributionHistory(APIView):
    def get(self, request: HttpResponse):
        contributors = ContributionHistory.objects.all()
        serializer = ContributionHistoryModelsSerializer(contributors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# CREATE OBJECTS
class CreateContributors(APIView):
   def post(self, request: HttpResponse, *args: Any, **kwargs: Any):
        data = request.data

        if not validate_fields(data['company'], data['description']):
            return Response({'error': 'Fields invalids'}, status=status.HTTP_400_BAD_REQUEST)

        serializers = ContributorsModelsSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        create_contributors_history = serializers.save()
        return Response({'success': 'Contribution made successfully!'}, status=status.HTTP_201_CREATED) 

class CreateContributionHistory(APIView):
    def post(self, request: HttpResponse):
        data = request.data

        if not validate_fields(data['company'], data['value']):
            return Response({'error': 'Fields invalids'}, status=status.HTTP_400_BAD_REQUEST)

        serializers = ContributionHistoryModelsSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        create_contributors = serializers.save()
        return Response({'success': 'Partnership made successfully. Thanks for your donation!'}, status=status.HTTP_201_CREATED)


# PICK UP AN OBJECTS
class GetContributionHistory(APIView):
    def get(self, request: HttpResponse, pk):
        contributors_history = get_object_or_404(ContributionHistory, pk=pk)

        if isinstance(contributors_history, ContributionHistory):
            response = {
                    'user': contributors_history.user,
                    'company': contributors_history.company,
                    'value': contributors_history.value,
                }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'contributors_history is not an instance of ContributionHistory'})

class GetContributors(APIView):
    def get(self, request: HttpResponse, pk):
        contributors = get_object_or_404(Contributors, pk=pk)

        if isinstance(contributors, Contributors):
            response = {
                    'user': contributors.user,
                    'company': contributors.company,
                    'description': contributors.description,
                    'role': contributors.role,
                }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'contributors is not an instance of Contributors'})    


# DELETE OBJECTS
class DeleteContributors(APIView):
    def delete(self, request: HttpResponse, pk):#eu renomeiei para delete
        contributors = get_object_or_404(Contributors, pk=pk)

        if isinstance(contributors, Contributors):
            contributors.delete()
            return Response({'success': 'Contributors deleted successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'contributors does not instance of Contributors'}, status=status.HTTP_400_BAD_REQUEST)