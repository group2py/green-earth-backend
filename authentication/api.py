# IMPORTS LIBRARIES PYTHON
from typing import Any

# IMPORTS DJANGO REST FRAMEWORK
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated

# IMPORTS DJANGO
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# IMPORTS FILES APP
from .models import Users
from .serializers import UsersModelsSerializer
from .utils import verify_password, validate_fields


class RegisterUser(ModelViewSet):
    # permission_classes = [IsAuthenticated, ]
    queryset = Users.objects.all()
    serializer_class = UsersModelsSerializer

    def list(self, request: HttpResponse):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request: HttpResponse):
        queryset = self.filter_queryset(self.get_queryset())
        data = request.data

        if not validate_fields(data['email'], data['password'], data['gender']):
            return Response({'error': 'fields invalid'}, serializer.data, status=status.HTTP_400_BAD_REQUEST)

        if not verify_password(request, data['password']):
            return Response({'error': 'password invalid'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token_JWT = RefreshToken.for_user(user)
        response = {
            'refresh': str(token_JWT),
            'access': str(token_JWT.access_token),
        }
        return Response(response, status=status.HTTP_201_CREATED)

    def retrieve(self, request: HttpResponse, pk):
        user = get_object_or_404(Users, pk=pk)

        if isinstance(user, Users):                
            reponse = {
                'image': user.image,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'password': user.password,
                'gender': user.gender,
                'phone': user.phone,
                'recovery_email': user.recorevy_email,
            }
            serializer = self.get_serializer(reponse)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'user is not an instance of Users'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request: HttpResponse, pk=None):
        instance = self.get_object()
        user = get_object_or_404(Users, pk=instance.id)

        if isinstance(user, Users):
            serializer = self.get_serializer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            return Response({'success': 'successfully changed data'}, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'User does not instance of Users'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request: HttpResponse, pk=None):
        instance_user = self.get_object()
        user = get_object_or_404(Users, pk=instance_user.id)

        if isinstance(user, Users):
            user.delete()
            return Response({'success': 'User deleted successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'User does not instance of Users'}, status=status.HTTP_400_BAD_REQUEST)
