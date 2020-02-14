from rest_framework import serializers
from .models import Part3


class Part3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Part3
        fields = '__all__'