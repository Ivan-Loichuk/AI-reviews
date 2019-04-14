from rest_framework import serializers

from application.models.hotel_models import CommentMapping


class CommentMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentMapping
        fields = '__all__'
