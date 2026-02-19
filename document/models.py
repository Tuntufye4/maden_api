from django.db import models
#from users.models import User
from property.models import Property    
        
class Document(models.Model):
    document_id = models.AutoField(primary_key=True)
 #   user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='document_user' )
    property_id = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, related_name='property_doc' )
    document_type = models.CharField(max_length=100)
    file_url = models.CharField(max_length=100)     
    created_at = models.DateTimeField()   
           