# from rest_framework import serializers
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as BaseUsersManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


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

    class GenderChoices(models.TextChoices):
        FEMENINE = 'F', 'Femenine'
        MASCULINE = 'M', 'Masculine'

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=False,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."  # noqa: E501
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    email = models.EmailField(
        _("email address"),
        blank=False,
        unique=True
    )

    image = models.ImageField(
        upload_to='image_profile'
    )

    gender = models.CharField(
        max_length=1,
        choices=GenderChoices.choices,
        blank=True,
        null=True
    )
    phone = models.IntegerField(blank=True, null=True)
    recovery_email = models.EmailField(blank=True, null=True)

    objects = UserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        # Todo defenir imagem automatico
        # self.image =
        super(Users, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Users'
