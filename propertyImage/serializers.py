from rest_framework import serializers
from .models import PropertyImage

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:                 
        model = PropertyImage      
        fields = "__all__"                     
                              