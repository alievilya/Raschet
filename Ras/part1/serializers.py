from rest_framework import serializers
from .models import Part1, Part1_2, Part1_3


class Part1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Part1
        fields = '__all__'

class Part1_2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Part1_2
        fields = '__all__'

class Part1_3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Part1_3
        fields = '__all__'

