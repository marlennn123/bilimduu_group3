from rest_framework import serializers
from .models import *


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarBetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBet
        fields = '__all__'

