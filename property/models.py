from django.db import models  


class Property(models.Model):
              
    title = models.CharField(max_length=100, null=True)
    description = models.TextField()
    property_type = models.CharField(max_length=50, null=True)
    listing_type = models.CharField(max_length=50, null=True)
    price = models.FloatField()
    is_negotiable = models.BooleanField(default=False)   
    size = models.IntegerField(null=True, blank=True)     
    bedrooms = models.IntegerField(null=True, blank=True)       
    bathrooms = models.IntegerField(null=True, blank=True)
    amenities = models.CharField(max_length=200, blank=True, null=True)  # Store amenities as list
    status = models.CharField(max_length=50, null=True)    
    country = models.CharField(max_length=50, null=True)
    region = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)   
    area = models.CharField(max_length=50, null=True)      
    image_url = models.ImageField(null=True)           
    display_order = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)             
          
    def __str__(self):   
        return self.title   