from rest_framework import serializers
from .models import MediaOng, CrimeDenunciations, BlogPost, FinancialResources


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

class FinancialResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialResources
        fields = '__all__'