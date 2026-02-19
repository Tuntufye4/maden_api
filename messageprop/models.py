# models.py
from django.db import models
from django.conf import settings        
from django.contrib.auth.models import User
from property.models import Property  # adjust import if your property model is in another app
            
class MessageProp(models.Model):
    user = models.ForeignKey(    
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,    
        related_name='message_prop'                       
    )
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    text_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)       
    
    def __str__(self):
        return f"Message from {self.user.username} for {self.property.id}"
                                      