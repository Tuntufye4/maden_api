from django.db import models
from django.conf import settings
from property.models import Property

class ViewingRequest(models.Model):
    viewingrequest_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='viewing_requests'    
    )
    property_id = models.ForeignKey(
        Property,                        
        on_delete=models.SET_NULL,                 
        null=True,    
        related_name='viewing_requests'               
    )    
    requested_date = models.DateField()   
    requested_time = models.DateTimeField()       
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ViewingRequest {self.viewingrequest_id} for {self.property}"
           