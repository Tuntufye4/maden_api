from django.db import models

class User(models.Model):        
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.CharField(max_length= 100)
    phone_number = models.IntegerField()
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100)                   
    is_verified = models.BooleanField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
            