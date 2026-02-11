from django.db import models
from property.models import Property 

class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    property_id = models.ForeignKey(Property, on_delete = models.SET_NULL, null=True, related_name ='message_prop')
    message_text = models.CharField(max_length=50)               
    is_read = models.BooleanField()
    created_at = models.DateTimeField()   
               