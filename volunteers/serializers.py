from .models import Volunteers
from rest_framework import serializers

class VolunteersModelsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Volunteers
        fields = '__all__'