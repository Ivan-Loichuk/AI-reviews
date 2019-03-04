from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from application.hotel_serializer import HotelSerializer
from application.models import Hotel


def registration(request):
    data = JSONParser().parse(request)
    user = User.objects.create_user(data['username'], data['email'], data['password'])
    user.last_name = data['lastname']
    user.first_name = data['firstname']
    user.save()
    return HttpResponse(201)


def auth(request):
    data = JSONParser().parse(request)
    username = data['username']
    password = data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse(None, status=401, safe=False)
    else:
        return JsonResponse(None, status=401, safe=False)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponse('')


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
