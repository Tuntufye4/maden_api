from rest_framework import serializers
from .models import ViewingRequest
from property.models import Property  
from property.serializers import PropertySerializer  # nested property info

class ViewingRequestSerializer(serializers.ModelSerializer):
    # Nested property info for frontend convenience
    property = PropertySerializer(read_only=True)
            
    # Write-only field to create/update viewing requests via property ID
    property = serializers.PrimaryKeyRelatedField(
        queryset=Property.objects.all(),
      #  source='property',  # maps to the ForeignKey
        write_only=True    
    )          
                 
    class Meta:   
        model = ViewingRequest
        fields = [           
            "id",   
            "user",
            "property",      # nested property info       # write-only for POST/PUT
            "requested_date",
            "requested_time",
            "created_at",
        ]
        read_only_fields = ["id", "user", "created_at"]
