from .models import Users, Genders
from rest_framework import serializers


class GendersModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genders
        fields = ('id', 'gender')


class UsersModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'gender', 'phone', 'recorevy_email')
        
