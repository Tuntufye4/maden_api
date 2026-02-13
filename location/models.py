# location/models.py
from django.db import models

class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.area}, {self.city}, {self.region}, {self.country}"
                   