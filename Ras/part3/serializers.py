from rest_framework import serializers
from .models import Part3, Part3_2, Part3_3


class Part3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Part3
        fields = '__all__'

class Part3_2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Part3_2
        fields = '__all__'

class Part3_3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Part3_3
        fields = '__all__'

