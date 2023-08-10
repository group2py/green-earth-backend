from typing import Any
from django.http.request import HttpRequest
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models import Q

UserModel = get_user_model()

class CustomBackends(ModelBackend):
    def authenticate(self, request: HttpRequest, username: str | None = ..., password: str | None = ..., **kwargs: Any) -> AbstractBaseUser | None:
        try:
            user = UserModel.objects.filter(
                Q(email__exact=username)
            )
            
        except UserModel.DoesNotExist:
            return
        
        if user.exists():
            my_user = user.first()
            if my_user.check_password(password):
                return my_user
                
            return
        else:
            return
    