# property/models.py
from django.db import models
from location.models import Location
#from user.models import User  # Optional owner

class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    property_type = models.CharField(max_length=50)
    listing_type = models.CharField(max_length=50)
    price = models.FloatField()
    is_negotiable = models.BooleanField(default=False)
    size = models.IntegerField(null=True, blank=True)
    bedrooms = models.IntegerField(null=True, blank=True)       
    bathrooms = models.IntegerField(null=True, blank=True)
    amenities = models.CharField(max_length=200, blank=True, null=True)  # Store amenities as list
    status = models.CharField(max_length=50)    
    # owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="properties")
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="properties",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.title
        