from django.db import models
#from user.models import User
from property.models import Property

class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
  #  user_id = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, related_name='user_res')
    property_id = models.ForeignKey(Property, on_delete= models.SET_NULL, null=True, related_name='property_res')
    booking_fee = models.FloatField()   
    expires_at = models.DateTimeField()           
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField()
      