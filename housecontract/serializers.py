from rest_framework import serializers
from .models import RentContract
from property.models import Property  
from property.serializers import PropertySerializer  # nested property info


class HouseContractSerializer(serializers.ModelSerializer):
    property_detail = PropertySerializer(source="property", read_only=True)
    property = serializers.PrimaryKeyRelatedField(queryset=Property.objects.all(), write_only=True)

    class Meta:       
        model = RentContract  
        fields = [
            "id",
            "user",
            "property",        # write-only
            "property_detail", # nested for GET
            "tenant_name",
            "tenant_email",
            "tenant_phone",
            "contract_startdate", 
            "created_at",             
        ]

        read_only_fields = ["id", "user", "created_at"]