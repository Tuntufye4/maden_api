from django.db import models
from user.models import User
from property.models import Property

class Offer(models.Model):
    offer_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, related_name='user_offer')             
    property_id = models.ForeignKey(Property, on_delete= models.SET_NULL, null=True, related_name='property_offer')
    offer_amount = models.FloatField()       
    status = models.CharField(max_length=100)      
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField()    