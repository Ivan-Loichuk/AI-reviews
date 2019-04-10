from application.models.hotel_models import HotelStatistic, Hotel
import asyncio


class StatisticsService:

    def compute_stats(self, map, hotel_id):
        self.__calc_stats_by_category(map, hotel_id)
        all_stat = self.__get_all_stats(hotel_id)
        hotel = Hotel.objects.get(id=hotel_id)
        hotel_stat = 0

        for val in enumerate(all_stat):
            hotel_stat += val.counter

        hotel.stat_summary = hotel_stat

        hotel.save()

    def __calc_stats_by_category(self, map, hotel_id):
        positive_stats = self.__get_stats('positive', map.category, hotel_id)
        negative_stats = self.__get_stats('negative', map.category, hotel_id)

        if map.comment_type == 'positive':
            positive_stats.counter += 1
        else:
            negative_stats.counter += 1
            negative_stats.save()

        positive_stats.stat = self.__calc_positives_percentage(positive_stats.counter, negative_stats.counter)
        positive_stats.save()

    @staticmethod
    def __calc_positives_percentage(positive, negative):
        return positive / (positive + negative) * 100

    @staticmethod
    def __get_stats(comment_type, category, hotel_id):
        return HotelStatistic.objects.filter(hotel=hotel_id, type=comment_type, category=category)

    @staticmethod
    def __get_all_stats(hotel_id):
        return HotelStatistic.objects.filter(hotel=hotel_id, type='positive')
