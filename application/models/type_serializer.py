from rest_framework import serializers

from application.models.hotel_models import HotelType


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelType
        fields = '__all__'
