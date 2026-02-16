from django.db import models
from property.models import Property

class PropertyImage(models.Model): 
    propertyimage_id = models.AutoField(primary_key=True)
    property_id = models.ForeignKey(Property, on_delete = models.SET_NULL, null=True, related_name ='property_img')
    image_url = models.ImageField()        
    display_order = models.CharField(max_length=100)
    created_at = models.DateTimeField()                        

    def __str__(self):
        return f"{self.display_order}"           