from rest_framework import serializers
from .models import Users

class UsersModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username', 'password', 'first_name', 'last_name',
                  'email', 'gender', 'phone', 'recovery_email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.is_active = False
        user.save()
        return user
