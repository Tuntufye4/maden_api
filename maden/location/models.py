from django.db import models

class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()        
    created_at = models.DateTimeField()