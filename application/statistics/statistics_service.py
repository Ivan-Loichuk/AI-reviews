from application.models.comment_mapping_serializer import CommentMappingSerializer
from application.models.hotel_models import HotelStatistic
import asyncio

from application.models.hotel_statistics_serializer import HotelStatisticSerializer


class StatisticsService:

    def compute_stats(self, comment, comment_mappings, hotel_id):
        self.__save_comment_mappings(comment, comment_mappings, hotel_id)

    def __save_comment_mappings(self, comment, comment_mappings, hotel_id):
        for index, value in enumerate(comment_mappings):
            comment_mapping = self.__create_comment_mapping(comment, value, hotel_id)
            comment_mapping_serializer = CommentMappingSerializer(data=comment_mapping)
            if comment_mapping_serializer.is_valid():
                comment_mapping_serializer.save()
            self.__save_hotel_stat(value, hotel_id)

    @staticmethod
    def __create_comment_mapping(comment, value, hotel_id):
        return {
                'comment': comment['comment'],
                'type': value.comment_type,
                'category': value.category,
                'hotel': hotel_id
        }

    def __save_hotel_stat(self, value, hotel_id):
        hotel_stats = self.__get_stats(hotel_id, value.category)
        self.__update_if_possible_hotel_stats(value, hotel_id, hotel_stats)

    def __update_if_possible_hotel_stats(self, value, hotel_id, hotel_stats):
        if not hotel_stats:
            hotel_stats = self.__create_hotel_stats(hotel_id, hotel_stats)
            hotel_stats[value.comment_type] += 1
            hotel_stat_serializer = HotelStatisticSerializer(data=hotel_stats)
            if hotel_stat_serializer.is_valid():
                hotel_stat_serializer.save()
        else:
            hotel_stats = hotel_stats[0]
            num = getattr(hotel_stats, value.comment_type)
            setattr(hotel_stats, value.comment_type, num + 1)
            hotel_stats.save()

    @staticmethod
    def __create_hotel_stats(hotel_id, value):
        return {
                'category': value.category,
                'positive': 0,
                'negative': 0,
                'hotel': hotel_id
        }

    @staticmethod
    def __get_stats(hotel_id, category):
        return HotelStatistic.objects.filter(hotel=hotel_id, category=category)

