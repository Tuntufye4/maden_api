from django.db import models
from django.conf import settings
from property.models import Property           
        
class ViewingRequest(models.Model):
    id = models.AutoField(primary_key=True)
   
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="viewing_requests"
    )   
    
    property = models.ForeignKey(   
        Property,
        on_delete=models.CASCADE,
        related_name="viewing_requests"   
    )      

    requested_date = models.DateField()
    requested_time = models.TimeField()
     
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} → {self.property} on {self.requested_date}"
                          