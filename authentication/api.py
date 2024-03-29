# IMPORTS PYTHON
import jwt

# IMPORTS DJANGO
from django.conf import settings
from django.http import HttpResponse
from django.utils.encoding import force_str
from django.shortcuts import get_object_or_404
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

# IMPORTS DJANGO REST FRAMEWORK
from rest_framework import status
from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response

# IMPORTS FILES APP
from .models import Users
from .backends import CustomBackends
from .serializers import UsersModelsSerializer
from .utils import validate_fields, verify_password

# Create token user jwt
def create_token(user_id: int) -> str:
    payload = dict(
        id=user_id,
    )
    token = jwt.encode(payload, settings.SECRET_KEY_JWT, algorithm="HS256")
    return token

class ListUsers(APIView):
    def get(self, request: HttpResponse):
        users = Users.objects.all()
        serializer = UsersModelsSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RegisterUser(APIView):

    def post(self, request: HttpResponse):
        data = request.data

        if not validate_fields(
            data['first_name'],
            data['email'], data['password']
        ):
            return Response(
                {'error': 'fields invalid'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not verify_password(
            request,
            data['password']
        ):
            return Response(
                {'error': 'password invalid'},
                status=status.HTTP_400_BAD_REQUEST
            )
    
        serializer = UsersModelsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {'success': 'Account created successfully'},
            status=status.HTTP_201_CREATED
        )

class UserDetails(APIView):

    def get(self, request: HttpResponse, pk):
        user = get_object_or_404(Users, pk=pk)

        if isinstance(user, Users):
            response = {
                'id': user.id,
                'image': user.image or None,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                "password": user.password,
                'email': user.email,
                'password': user.password,
                'gender': user.gender,
                'phone': user.phone,
                'recovery_email': user.recovery_email,
            }

            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(
                {'instance error': 'user is not an instance of Users'},
                status=status.HTTP_400_BAD_REQUEST
            )

class UserUpdate(APIView):
    def get(self, request: HttpResponse, pk):
        user = get_object_or_404(Users, pk=pk)
        serializer = UsersModelsSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: HttpResponse, pk):
        user = get_object_or_404(Users, pk=pk)

        if isinstance(user, Users):
            data = request.data

            if not validate_fields(
                data['first_name'],
                data['gender']
            ):
                return Response(
                    {'error': 'fields invalids'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            image = request.FILES['image']
            user.image = image
            user.username = data['first_name']
            user.first_name = data['first_name'] or user.first_name
            user.last_name = data['last_name'] or user.last_name
            user.gender = data['gender']
            user.phone = data['phone'] or user.phone
            user.recovery_email = data['recovery_email'] or user.recovery_email
            user.save()
            return Response(
                {'success': 'successfully changed data'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'instance error': 'User does not instance of Users'},
                status=status.HTTP_400_BAD_REQUEST
            )

class ActivateAccountView(APIView):

    def get(self, request: HttpResponse, uid4, token):
        uid = force_str(urlsafe_base64_decode(uid4))
        user = get_object_or_404(Users, pk=uid)

        if (user := user.first()) and \
                default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()

            return Response({'account_activated': 'Account activated successfully',}, status=status.HTTP_200_OK)
        else:
            return Response(
                {'error': 'Invalid activation link.'},
                status=status.HTTP_400_BAD_REQUEST
            )

class LoginUser(APIView):
    def post(self, request: HttpResponse):
        data = request.data

        if not validate_fields(data['email'], data['password']):
            return Response(
                {'error': 'fields invalid'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user = CustomBackends().authenticate(request, username=data['email'], password=data["password"])
        if user is None:
            return Response(
                {'error': 'invalid email or password'},
                status=status.HTTP_400_BAD_REQUEST
            )

        token = create_token(user_id=user.pk)
        resp = response.Response({'success': 'user logged in successfully', 'token': token})

        return resp