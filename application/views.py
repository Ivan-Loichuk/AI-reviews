from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.core import serializers
import json

from application.comment_serializer import CommentSerializer
from application.hotel_serializer import HotelSerializer
from application.models import Hotel, Comment
from application.type_serializer import TypeSerializer


def create_hotel(request):
    data = JSONParser().parse(request)
    hotel_serializer = HotelSerializer(data=data)
    if hotel_serializer.is_valid():
        hotel_serializer.save()
        return JsonResponse(hotel_serializer.data, status=201)
    return JsonResponse(hotel_serializer.errors, status=400)


def get_hotels(request):
    hotels = Hotel.objects.all().values()
    #serialized_obj = serializers.serialize('json', hotels)
    return JsonResponse(list(hotels), content_type="application/json", safe=False)


def get_hotel(request, hotel_id):
    hotel = Hotel.objects.filter(id=hotel_id).values()[0]
    #serialized_obj = serializers.serialize('json', [hotel])
    return JsonResponse(hotel, content_type="application/json", safe=False)


#@login_required
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

