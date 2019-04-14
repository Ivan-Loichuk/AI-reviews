from django.contrib.auth.models import User
from django.db import models


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
    stat_summary = models.IntegerField()


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)


class CommentMapping(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=256)
    type = models.CharField(max_length=256)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


class HotelStatistic(models.Model):
    id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    category = models.CharField(max_length=256)

    staff_positive_counter = models.IntegerField()
    staff_negative_counter = models.IntegerField()

    location_positive_counter = models.IntegerField()
    location_negative_counter = models.IntegerField()

    cleanliness_positive_counter = models.IntegerField()
    cleanliness_negative_counter = models.IntegerField()

    food_positive_counter = models.IntegerField()
    food_negative_counter = models.IntegerField()

    facilities_positive_counter = models.IntegerField()
    facilities_negative_counter = models.IntegerField()

    total_positive_counter = models.IntegerField()
    total_negative_counter = models.IntegerField()
