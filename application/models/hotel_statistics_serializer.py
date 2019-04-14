from rest_framework import serializers

from application.models.hotel_models import HotelStatistic


class HotelStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelStatistic
        fields = '__all__'
