from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import UserManager as BaseUsersManager, AbstractUser


class UserManager(BaseUsersManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

class Users(AbstractUser):
    choice_gender = (
        ('F', 'Femenine'),
        ('M', 'Masculine'),
    )
    username = models.CharField(max_length=150, unique=False, blank=True, null=True)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='image_profile', blank=True, null=True)
    gender = models.CharField(max_length=1, choices=choice_gender, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    recovery_email = models.EmailField(blank=True, null=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        self.image = 'static/authentication/img/profile.png'
        super(Users, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Users'
