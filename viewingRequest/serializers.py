from rest_framework import serializers
from .models import ViewingRequest
from property.models import Property
from property.serializers import PropertySerializer  # optional, for nested property

class ViewingRequestSerializer(serializers.ModelSerializer):
    # Nested property info for frontend convenience
    property = PropertySerializer(read_only=True, source='property_id')
    # Send property ID when creating/updating
    property_id = serializers.PrimaryKeyRelatedField(
        queryset=Property.objects.all(),
        source='property_id',
        write_only=True
    )

    class Meta:   
        model = ViewingRequest
        fields = [   
            "id",            # standard PK
            "user",          # read-only
            "property",      # nested read-only
            "property_id",   # write-only
            "requested_date",
            "requested_time",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "user", "created_at", "updated_at"]
                    