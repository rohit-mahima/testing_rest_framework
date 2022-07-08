from re import A
from statistics import mode
from rest_framework import serializers
from .models import Artifiact

class ArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifiact
        fields="__all__"