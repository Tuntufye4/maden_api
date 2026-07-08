from rest_framework import serializers
from .models import ViewingRequest
from property.models import Property  
from property.serializers import PropertySerializer  # nested property info
from users.models import User
from users.serializers import UserSerializer
  
     

class ViewingRequestSerializer(serializers.ModelSerializer):
    property_detail = PropertySerializer(source="property", read_only=True)
    user_detail = UserSerializer(source="user", read_only=True)  
    property = serializers.PrimaryKeyRelatedField(queryset=Property.objects.all(), write_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)

    class Meta:
        model = ViewingRequest
        fields = [
            "id",    
            "user",
            "property",        # write-only
            "property_detail", # nested for GET
            "user_detail",   
            "requested_date",
            "requested_time",     
            "created_at",
        ]

        read_only_fields = ["id", "user", "created_at"]