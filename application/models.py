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
    name = models.CharField(max_length=4096)
    city = models.CharField(max_length=256)
    street = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    hotel_type = models.ForeignKey(HotelType, on_delete=models.CASCADE)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
