# IMPORTS LIBRARIES PYTHON
from typing import Any
import json
# IMPORTS DJANGO REST FRAMEWORK
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# IMPORTS DJANGO
from django.http import HttpResponse
from django.utils.encoding import force_str
from django.shortcuts import get_object_or_404
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

# IMPORTS FILES APP
from .models import Users, Genders
from .activate_account import ActivateAccount
from .serializers import UsersModelsSerializer
from .utils import verify_password, validate_fields

class ListUsers(APIView):
    def get(self, request: HttpResponse):
        users = Users.objects.all()
        serializer = UsersModelsSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RegisterUser(APIView):
    def post(self, request: HttpResponse):
        data = request.data

        if not validate_fields(data['first_name'], data['email'], data['password']):
            return Response({'error': 'fields invalid'}, status=status.HTTP_400_BAD_REQUEST)

        if not verify_password(request, data['password']):
            return Response({'error': 'password invalid'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UsersModelsSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save(is_active=False)
        return Response({'success': 'Account created successfully'}, status=status.HTTP_201_CREATED)
    
class UserDetails(APIView):
    def get(self, request: HttpResponse, pk):
        user = get_object_or_404(Users, pk=pk)

        if isinstance(user, Users):                
            response = {
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'password': user.password,
                'gender': user.gender,
                'phone': user.phone,
                'recorevy_email': user.recorevy_email,
            }
            
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'user is not an instance of Users'}, status=status.HTTP_400_BAD_REQUEST)

class UserUpdate(APIView):
    def get(self, request: HttpResponse, pk):
        user = get_object_or_404(Users, pk=pk)
        serializer = UsersModelsSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: HttpResponse, pk):
        user = get_object_or_404(Users, pk=pk)

        if isinstance(user, Users):
            data = request.data
            
            if not validate_fields(data['first_name'], data['gender']):
                return Response({'error': 'fields invalids'}, status=status.HTTP_400_BAD_REQUEST)

            user.username = data['username']
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.email = data['email']
            user.password = data['password']
            user.gender = get_object_or_404(Genders, pk=data['gender'])
            user.phone = data['phone']
            user.recorevy_email = data['recorevy_email']
            user.save()
            return Response({'success': 'successfully changed data'}, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'User does not instance of Users'}, status=status.HTTP_400_BAD_REQUEST)

class UserDelete(APIView):
    def delete(self, request: HttpResponse, pk, *args, **kwargs):
        user = get_object_or_404(Users, pk=pk)
        print('1')
        if isinstance(user, Users):
            user.delete()
            return Response({'success': 'User deleted successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'User does not instance of Users'}, status=status.HTTP_400_BAD_REQUEST)

class ActivateAccountView(APIView):
    def get(self, request: HttpResponse, uid4, token):
        uid = force_str(urlsafe_base64_decode(uid4))
        user = get_object_or_404(Users, pk=uid)
        
        if (user := user.first()) and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()

            token_JWT = RefreshToken.for_user(user)
            response = {
                'refresh': str(token_JWT),
                'access': str(token_JWT.access_token),
                'account_activated': 'Account activated successfully',
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid activation link.'}, status=status.HTTP_400_BAD_REQUEST)