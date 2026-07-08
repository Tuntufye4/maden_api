from rest_framework import serializers
from .models import RentContract
from property.models import Property  
from property.serializers import PropertySerializer
from users.models import User  # nested property info
from users.serializers import UserSerializer


class HouseContractSerializer(serializers.ModelSerializer):
    property_detail = PropertySerializer(source="property", read_only=True)
    property = serializers.PrimaryKeyRelatedField(queryset=Property.objects.all(), write_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    user_detail = UserSerializer(source="user", read_only=True)  
   


    class Meta:       
        model = RentContract  
        fields = [   
            "id",
            "user",
            "property",        # write-only
            "property_detail", # nested for GET    
            "tenant_name",   
            "user_detail",                  
            "tenant_email",
            "tenant_phone",          
            "contract_startdate", 
            "created_at",                   
        ]

        read_only_fields = ["id", "user", "created_at"]                 