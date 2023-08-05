from typing import Any
from rest_framework import serializers
from .models import Contributors, ContributionHistory


class ContributorsModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributors
        fields = '__all__'

class ContributionHistoryModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContributionHistory
        fields = '__all__'
