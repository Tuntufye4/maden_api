from django.db import models
from user.models import User
from property.models import Property       

class ViewingRequest(models.Model):
    viewingrequest_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete = models.SET_NULL, null=True, related_name = 'user_view')
    property_id = models.ForeignKey(Property, on_delete = models.SET_NULL, null=True, related_name = 'property_view')
    requested_date = models.DateField()
    requested_time = models.DateTimeField()      
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField()   