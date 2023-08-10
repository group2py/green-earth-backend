from .models import Users
from rest_framework import serializers

class UsersModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'gender', 'phone', 'recovery_email')