from rest_framework import serializers
from .models import PropertyImage

class propertyImageSerializer(serializers.ModelSerializer):
    class Meta:                 
        model = PropertyImage      
        fields = "__all__"                     
             