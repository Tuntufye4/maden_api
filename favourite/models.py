from django.db import models
#from user.models import User
from property.models import Property

class Favourite(models.Model):
    favourite_id = models.AutoField(primary_key=True)
 #   user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_fav')
    property_id = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, related_name='property_fav')
    created_at = models.DateTimeField()                   