from rest_framework import serializers
from .models import Part1, Page1BezRazdel, Page1BezSostav, Part1_3
from .models import Page1Recogn, Page1TimeMarsh, Page1TimeRazv

from .models import Page1OneWay1, Page1RazOneSostav1, Page1Recogn1, Page1TimeMarsh1, Page1TimeRazv1
from .models import Page1CoupleWays1, Page1RazCoupleSostav1, Page1Recogn2, Page1TimeMarsh2, Page1TimeRazv2

class Part1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Part1
        fields = '__all__'

class Page1BezRazdelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page1BezRazdel
        fields = '__all__'

class Page1BezSostavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page1BezSostav
        fields = '__all__'

class Page1TimeMarshSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page1TimeMarsh
        fields = '__all__'

class Page1TimeRazvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page1TimeRazv
        fields = '__all__'
class Page1RecognSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page1Recogn
        fields = '__all__'



class Page1OneWay1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Page1OneWay1
        fields = '__all__'

class Page1RazOneSostav1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Page1RazOneSostav1
        fields = '__all__'

class Page1Recogn1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Page1Recogn1
        fields = '__all__'

class Page1TimeMarsh1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Page1TimeMarsh1
        fields = '__all__'

class Page1TimeRazv1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Page1TimeRazv1
        fields = '__all__'





class Page1CoupleWays1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Page1CoupleWays1
        fields = '__all__'

class Page1RazCoupleSostav1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Page1RazOneSostav1
        fields = '__all__'

class Page1Recogn2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Page1Recogn2
        fields = '__all__'

class Page1TimeMarsh2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Page1TimeMarsh2
        fields = '__all__'

class Page1TimeRazv2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Page1TimeRazv2
        fields = '__all__'








class Part1_3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Part1_3
        fields = '__all__'

