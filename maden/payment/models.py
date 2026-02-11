from django.db import models
from property.models import Property
from reservation.models import Reservation
from user.models import User

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_pay' )
    property_id = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True ,  related_name='property_pay')
    reservation_id = models.ForeignKey(Reservation, on_delete=models.SET_NULL, null=True, related_name='reservation_pay')
    amount = models.FloatField()
    payment_type = models.CharField(max_length=100)            
    payment_method = models.CharField(max_length=100)    
    transaction_reference = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField()