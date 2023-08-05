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

class Genders(models.Model):
    choice_gender = (
        ('F', 'Femenine'),
        ('M', 'Masculine'),
    )

    gender = models.CharField(
        max_length=1,
        choices=choice_gender
    )

    def __str__(self):
        return self.gender

    class Meta:
        verbose_name_plural = 'Genders'

class Users(AbstractUser):
    username = models.CharField(max_length=150, unique=False)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='image_profile')
    gender = models.ForeignKey(Genders, on_delete=models.DO_NOTHING, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    recorevy_email = models.EmailField(blank=True, null=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"

    objects = UserManager()

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        # TODO defenir imagem automatico
        # self.image = 
        super(Users, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Users'

class User(models.Model):
    name = models.CharField(max_length=100)
    