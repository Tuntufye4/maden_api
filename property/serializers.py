from rest_framework import serializers
from .models import Property
from location.models import Location
from location.serializers import LocationSerializer
from propertyImage.models import PropertyImage    
from propertyImage.serializers import PropertyImageSerializer    

class PropertySerializer(serializers.ModelSerializer):
    # Nested location input/output   
    location = LocationSerializer(source="location_id", required=False)
    # Nested property images
    images = PropertyImageSerializer(
        source="property_img",  # match related_name in PropertyImage model
        many=True,
        required=False  
    )   

    class Meta:
        model = Property
        fields = "__all__"

    def create(self, validated_data):
        # ---------------- HANDLE NESTED LOCATION ----------------
        location_data = validated_data.pop("location_id", None)
        if location_data:
            location, _ = Location.objects.get_or_create(
                region=location_data.get("region", "").strip(),
                city=location_data.get("city", "").strip(),
                area=location_data.get("area", "").strip()
            )
            validated_data["location_id"] = location

        # ---------------- HANDLE NESTED IMAGES ----------------
        images_data = validated_data.pop("property_img", [])

        # Create the Property instance first
        property_instance = super().create(validated_data)
      
        # Create PropertyImage instances
        for idx, img_data in enumerate(images_data):
            PropertyImage.objects.create(
                property=property_instance,
                image_url=img_data.get("image_url"),
                display_order=img_data.get("display_order", idx + 1)
            )

        return property_instance
    