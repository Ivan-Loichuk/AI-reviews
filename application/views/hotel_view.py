from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.parsers import JSONParser


from application.models.comment_serializer import CommentSerializer
from application.models.hotel_serializer import HotelSerializer
from application.models.hotel_models import Hotel, Comment, HotelType, HotelStatistic, CommentMapping
from application.models.type_serializer import TypeSerializer
from application.statistics.network import Model
from application.statistics.statistics_service import StatisticsService

statisticsService = StatisticsService()


@login_required
def create_hotel(request):
    data = JSONParser().parse(request)
    hotel_serializer = HotelSerializer(data=data)
    if hotel_serializer.is_valid():
        hotel_serializer.save()
        return JsonResponse(hotel_serializer.data, status=201)
    return JsonResponse(hotel_serializer.errors, status=400)


def get_hotels():
    hotels = Hotel.objects.all().values()
    return JsonResponse(list(hotels), content_type="application/json", safe=False)


def search_hotels(request):
    data = JSONParser().parse(request)
    if data['types'] and not data['city'] == '':
        hotels = Hotel.objects.filter(hotel_type__type__in=data['types'], city__icontains=data['city']).values()
    elif data['types']:
        hotels = Hotel.objects.filter(hotel_type__type__in=data['types']).values()
    elif not data['city'] == '':
        hotels = Hotel.objects.filter(city__icontains=data['city']).values()
    else:
        hotels = hotels = Hotel.objects.all().values()
    return JsonResponse(list(hotels), content_type="application/json", safe=False)


def get_hotel(request, hotel_id):
    hotel = Hotel.objects.filter(id=hotel_id).values()[0]
    hotel_type = HotelType.objects.filter(id=(hotel['hotel_type_id'])).values()[0]
    hotel['hotel_type'] = hotel_type['type']
    return JsonResponse(hotel, content_type="application/json", safe=False)


@login_required
def add_comment(request):
    data = JSONParser().parse(request)
    user = request.user
    data['sender'] = User.objects.get(username=user).id
    comment_serializer = CommentSerializer(data=data)
    if comment_serializer.is_valid():
        id = comment_serializer.save().id
        comment = {'comment': id, 'content': data['content']}
        map_comment(comment, data['hotel'])
        return JsonResponse(comment_serializer.data, status=201)
    return JsonResponse(comment_serializer.errors, status=500)


def map_comment(comment, hotel_id):
    model = Model()
    comment_parts = comment['content'].split('.')
    comment_mappings = []
    for index, value in enumerate(comment_parts):
        if not value == '':
            comment_mappings.append(model.use_neural_network(value))
    statisticsService.compute_stats(comment, comment_mappings, hotel_id)


def add_hotel_type(request):
    data = JSONParser().parse(request)
    type_serializer = TypeSerializer(data=data)
    if type_serializer.is_valid():
        type_serializer.save()
        return JsonResponse(type_serializer.data, status=201)
    return JsonResponse(type_serializer.errors, status=400)


def get_comments(request, hotel_id):
    comments = Comment.objects.filter(hotel=hotel_id).values()
    for index, val in enumerate(comments):
        user = User.objects.filter(id=val['sender_id']).values()[0]
        comments[index]['sender'] = user['username']
    return JsonResponse(list(comments), content_type="application/json", safe=False)


def get_statistic(request, hotel_id):
    statistic = HotelStatistic.objects.filter(hotel=hotel_id).values()
    return JsonResponse(list(statistic), content_type="application/json", safe=False)


def get_comment_mappings(request, hotel_id):
    comment_mappings = CommentMapping.objects.filter(hotel=hotel_id).values()
    return JsonResponse(list(comment_mappings), content_type="application/json", safe=False)
