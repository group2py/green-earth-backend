from .models import Volunteers, NewMission
from rest_framework import serializers

class VolunteersModelsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Volunteers
        fields = '__all__'

class NewMissionModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewMission
        fields = '__all__'
