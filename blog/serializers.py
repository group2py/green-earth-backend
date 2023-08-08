from rest_framework import serializers
from .models import MediaOng, CrimeDenunciations, BlogPost, NewMission


class CrimeDenunciationsModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrimeDenunciations
        fields = '__all__'

class MediaOngModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaOng
        fields = '__all__'

class BlogPostModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

class NewMissionModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewMission
        fields = '__all__'
