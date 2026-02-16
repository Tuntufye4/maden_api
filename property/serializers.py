from rest_framework import serializers
from .models import Property
from location.models import Location
from location.serializers import LocationSerializer
from propertyImage.models import PropertyImage
from propertyImage.serializers import PropertyImageSerializer


class PropertySerializer(serializers.ModelSerializer):
    # Nested location input/output
    location = LocationSerializer(source="location_id", required=False)
    # Nested property images (ordered)
    images = PropertyImageSerializer(     
        source="property_img",  # matches related_name in PropertyImage model
        many=True,
        required=False,
        read_only=False
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

        # Bulk create images (skip empty URLs)
        image_objs = []
        for idx, img_data in enumerate(images_data):
            image_url = img_data.get("image_url")
            if not image_url:
                continue
            image_objs.append(
                PropertyImage(
                    property=property_instance,
                    image_url=image_url,
                    display_order=img_data.get("display_order", idx + 1)
                )
            )
        if image_objs:
            PropertyImage.objects.bulk_create(image_objs)

        return property_instance

    def to_representation(self, instance):
        """Ensure images are returned ordered by display_order"""
        rep = super().to_representation(instance)
        rep["images"] = PropertyImageSerializer(
            instance.property_img.order_by("display_order"), many=True
        ).data
        return rep
        