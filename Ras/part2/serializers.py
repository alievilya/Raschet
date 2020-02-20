from rest_framework import serializers
from .models import Part2, Part2_2

class Part2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Part2
        fields = '__all__'

class Part2_2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Part2_2
        fields = '__all__'
