from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from application.hotel_serializer import HotelSerializer
from application.models import Hotel


@login_required
def create_hotel(request):
    data = JSONParser().parse(request)
    hotel_serializer = HotelSerializer(data=data)
    if hotel_serializer.is_valid():
        hotel_serializer.save()
        return JsonResponse(hotel_serializer.data, status=201)
    return JsonResponse(hotel_serializer.errors, status=400)


@login_required
def get_hotels(request):
    print(request.user)
    hotels = Hotel.objects.all()
    hotel_serializer = HotelSerializer(hotels, many=True)
    return JsonResponse(hotel_serializer.data, safe=False)
