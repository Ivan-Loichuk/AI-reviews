from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from application.models.comment_serializer import CommentSerializer
from application.models.hotel_serializer import HotelSerializer
from application.models.models import Hotel, Comment
from application.models.type_serializer import TypeSerializer


#@login_required
def create_hotel(request):
    data = JSONParser().parse(request)
    hotel_serializer = HotelSerializer(data=data)
    if hotel_serializer.is_valid():
        hotel_serializer.save()
        return JsonResponse(hotel_serializer.data, status=201)
    return JsonResponse(hotel_serializer.errors, status=400)


def get_hotels(request):
    hotels = Hotel.objects.all().values()
    return JsonResponse(list(hotels), content_type="application/json", safe=False)


def search_hotels(request, city):
    hotels = Hotel.objects.filter(city=city).values();
    return JsonResponse(list(hotels), content_type="application/json", safe=False)


def get_hotel(request, hotel_id):
    hotel = Hotel.objects.filter(id=hotel_id).values()[0]
    return JsonResponse(hotel, content_type="application/json", safe=False)


@login_required
def add_comment(request):
    data = JSONParser().parse(request)
    comment_serializer = CommentSerializer(data=data)
    if comment_serializer.is_valid():
        comment_serializer.save()
        return JsonResponse(comment_serializer.data, status=201)
    return JsonResponse(comment_serializer.errors, status=400)


def add_hotel_type(request):
    data = JSONParser().parse(request)
    type_serializer = TypeSerializer(data=data)
    if type_serializer.is_valid():
        type_serializer.save()
        return JsonResponse(type_serializer.data, status=201)
    return JsonResponse(type_serializer.errors, status=400)


def get_comments(request, hotel_id):
    comments = Comment.objects.filter(hotel=hotel_id).values()
    return JsonResponse(list(comments), content_type="application/json", safe=False)

