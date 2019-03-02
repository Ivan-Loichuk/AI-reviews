from django.db import models


class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2000)
    # city = models.CharField(max_length=200)
    # street = models.CharField(max_length=200)

    def __str__(self):
        return 'Hotel name: ' + self.name
