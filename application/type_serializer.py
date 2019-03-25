from rest_framework import serializers
from application.models import Hotel, HotelType


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelType
        fields = '__all__'
