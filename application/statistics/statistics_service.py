from application.models.comment_mapping_serializer import CommentMappingSerializer
from application.models.hotel_models import HotelStatistic, Hotel
import asyncio


class StatisticsService:

    def compute_stats(self, comment, comment_mappings, hotel_id):
        self.save_comment_mappings(comment, comment_mappings)
        hotel_stats = self.__get_stats(hotel_id)
        print(hotel_stats)

    @staticmethod
    def save_comment_mappings(comment, comment_mappings):
        for index, value in enumerate(comment_mappings):
            comment_mapping = {
                'comment': comment['comment'],
                'type': value.comment_type,
                'category': value.category
            }
            comment_mapping_serializer = CommentMappingSerializer(data=comment_mapping)
            if comment_mapping_serializer.is_valid():
                comment_mapping_serializer.save()

    @staticmethod
    def __calc_positives_percentage(positive, negative):
        return positive / (positive + negative) * 100

    @staticmethod
    def __get_stats(hotel_id):
        return HotelStatistic.objects.filter(hotel=hotel_id)

