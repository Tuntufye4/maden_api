from rest_framework import serializers
from .models import ViewingRequest

class ViewingRequestSerializer(serializers.ModelSerializer):
    class Meta:                 
        model = ViewingRequest              
        fields = "__all__"           
                        