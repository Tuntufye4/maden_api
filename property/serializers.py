from rest_framework import serializers
from .models import Property
from location.models import Location
from location.serializers import LocationSerializer

class PropertySerializer(serializers.ModelSerializer):
    # Nested location input/output
    location = LocationSerializer(source="location_id", required=False)

    class Meta:
        model = Property
        fields = "__all__"

    def create(self, validated_data):
        # Handle nested location
        location_data = validated_data.pop("location_id", None)
        if location_data:
            location, _ = Location.objects.get_or_create(
                region=location_data.get("region", "").strip(),
                city=location_data.get("city", "").strip(),
                area=location_data.get("area", "").strip(),               
                defaults={
                  #  "country": location_data.get("country", ""),    
                    "latitude": location_data.get("latitude", 0.0),
                    "longitude": location_data.get("longitude", 0.0),
                    "created_at": location_data.get("created_at"),
                },
            )
            validated_data["location_id"] = location

        return super().create(validated_data)
   