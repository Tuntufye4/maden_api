from django.db import models
#from user.models import User
from location.models import Location             

class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    property_type = models.CharField(max_length=50)
    listing_type = models.CharField(max_length=50)
    price = models.FloatField()
    is_negotiable = models.BooleanField()
    size = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    amenities = models.IntegerField()
    status = models.CharField(max_length=100)
   # owner_id = models.ForeignKey(User, on_delete = models.SET_NULL, null= True, related_name = 'user_prop')
    location_id = models.ForeignKey(Location, on_delete = models.SET_NULL , null= True, related_name ='location_prop') 
    created_at = models.DateTimeField()   
    updated_at = models.DateTimeField()
     