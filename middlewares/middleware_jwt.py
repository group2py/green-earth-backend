from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from rest_framework_simplejwt.tokens import AccessToken

def jwt_middleware(get_response):
    def middleware(request):
        authorization_header = request.META.get('HTTP_AUTHORIZATION')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            return Response({'error': 'Authorization header missing or invalid'}, status=status.HTTP_401_UNAUTHORIZED)

        token = authorization_header.split(' ')[1]

        try:
            access_token = AccessToken(token)
            if not access_token['token_type'] == 'access':
                raise AccessToken.DoesNotExist

            request.user = access_token.payload.get('user_id')
        except AccessToken.DoesNotExist:
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

        response = get_response(request)
        return response

    return middleware