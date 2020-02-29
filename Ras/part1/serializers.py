from rest_framework import serializers
from .models import Part1, Page1BezRazdel, Page1OneWay1,Page1OneWay2, Page1CoupleWays1, Page1CoupleWays2, Part1_3


class Part1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Part1
        fields = '__all__'

class Page1BezRazdelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page1BezRazdel
        fields = '__all__'

class Page1OneWay1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Page1OneWay1
        fields = '__all__'

class Page1OneWay2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Page1OneWay2
        fields = '__all__'

class Page1CoupleWays1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Page1CoupleWays1
        fields = '__all__'

class Page1CoupleWays2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Page1BezRazdel
        fields = '__all__'

class Part1_3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Part1_3
        fields = '__all__'

