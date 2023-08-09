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
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get(
            'username',
            instance.username
        )
        instance.first_name = validated_data.get(
            'first_name',
            instance.first_name
        )
        instance.last_name = validated_data.get(
            'last_name',
            instance.last_name
        )
        instance.email = validated_data.get(
            'email',
            instance.email
        )
        instance.gender = validated_data.get(
            'gender',
            instance.gender
        )
        instance.phone = validated_data.get(
            'phone',
            instance.phone
        )
        instance.recovery_email = validated_data.get(
            'recovery_email',
            instance.recovery_email
        )

        instance.set_password(
            validated_data.get('password', instance.password)
        )

        instance.save()
        return instance
