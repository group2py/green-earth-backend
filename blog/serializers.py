from rest_framework import serializers
from .models import MediaOng, CrimeDenunciations, BlogPost


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
