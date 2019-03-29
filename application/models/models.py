from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class HotelType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=1024)


class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    street = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    hotel_type = models.ForeignKey(HotelType, on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
