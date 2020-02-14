from rest_framework import serializers
from .models import Part4


class Part4Serializer(serializers.ModelSerializer):
    class Meta:
        model = Part4
        fields = '__all__'