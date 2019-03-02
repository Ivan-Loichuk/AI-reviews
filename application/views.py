from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from application.hotel_serializer import HotelSerializer
from application.models import Hotel


@api_view(['GET'])
def index(request):
    return HttpResponse("Hello, world. You're at the index.")


@api_view(['POST'])
def create_hotel(request):
    data = JSONParser().parse(request)
    hotel_serializer = HotelSerializer(data=data)
    if hotel_serializer.is_valid():
        hotel_serializer.save()
        return JsonResponse(hotel_serializer.data, status=201)
    return JsonResponse(hotel_serializer.errors, status=400)


def get_hotels(request):
    hotels = Hotel.objects.all()
    hotel_serializer = HotelSerializer(hotels, many=True)
    return JsonResponse(hotel_serializer.data, safe=False)
