import jwt
from .models import Users
from django.conf import settings
from rest_framework import authentication, exceptions

class CustomUserAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get("jwt")

        if not token:
            return None
        try:
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        except:
            raise exceptions.AuthenticationFailed("Unauthorized")

        user = Users.objects.filter(id=payload["id"]).first()
        return (user, None)