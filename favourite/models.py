from django.db import models
from django.conf import settings     
from property.models import Property
                
class Favourite(models.Model):
    favourite_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(   
        settings.AUTH_USER_MODEL,      
        on_delete=models.CASCADE,
        related_name="favourite", null=True      
    )         
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, related_name='property_fav')
    created_at = models.DateTimeField(null=True)                                
    is_favourite = models.BooleanField(default=False, null=True)                                                