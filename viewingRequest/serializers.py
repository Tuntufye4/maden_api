from rest_framework import serializers
from .models import ViewingRequest
from property.models import Property  
from property.serializers import PropertySerializer  # nested property info


class ViewingRequestSerializer(serializers.ModelSerializer):
    property_detail = PropertySerializer(source="property", read_only=True)
    property = serializers.PrimaryKeyRelatedField(queryset=Property.objects.all(), write_only=True)

    class Meta:
        model = ViewingRequest
        fields = [
            "id",
            "user",
            "property",        # write-only
            "property_detail", # nested for GET
            "requested_date",
            "requested_time",  
            "created_at",
        ]

        read_only_fields = ["id", "user", "created_at"]