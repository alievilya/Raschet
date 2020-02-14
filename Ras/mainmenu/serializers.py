from rest_framework import serializers
from .models import Mainmenu


class MainmenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mainmenu
        fields = '__all__'