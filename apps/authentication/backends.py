from typing import Any
from django.http.request import HttpRequest
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser


class CustomBackends(ModelBackend):
    def authenticate(self, request: HttpRequest, email: str | None = ..., password: str | None = ..., **kwargs: Any) -> AbstractBaseUser | None:
        try:
            User = get_user_model()
            user = User.objects.filter(
                email__exact=email
            )
        except user.DoesNotExist:
            return
        
        if user.exists():
            my_user = user.first()
            if my_user.check_password(password):
                return my_user
            
            return
        
        return