from rest_framework import serializers
from .models import Part4, Part4_2, Part4_3

class Part4Serializer(serializers.ModelSerializer):
    class Meta:
        model = Part4
        fields = '__all__'

class Part4_2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Part4_2
        fields = '__all__'

class Part4_3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Part4_3
        fields = '__all__'