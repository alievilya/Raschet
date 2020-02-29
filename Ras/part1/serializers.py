from rest_framework import serializers
from .models import Part1, Page1BezRazdel, Part1_3


class Part1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Part1
        fields = '__all__'

class Page1BezRazdelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page1BezRazdel
        fields = '__all__'

class Part1_3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Part1_3
        fields = '__all__'

