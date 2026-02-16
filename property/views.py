from django.db import transaction
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Property
from .serializers import PropertySerializer    
from propertyImage.models import PropertyImage
from propertyImage.serializers import PropertyImageSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    """
    CRUD for Properties.
    Handles nested Location and bulk PropertyImages via serializer.
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def create(self, request, *args, **kwargs):
        """
        Create a Property with optional nested Location and multiple images.
        """
        with transaction.atomic():
            data = request.data.copy()

            # ---------------- HANDLE NESTED LOCATION ----------------
            region = data.pop("region", None)
            city = data.pop("city", None)
            area = data.pop("area", None)
            location = None
            if region and city and area:
                from location.models import Location
                location, _ = Location.objects.get_or_create(
                    region=region.strip(),
                    city=city.strip(),
                    area=area.strip()
                )

            # ---------------- CREATE PROPERTY ----------------
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            property_instance = serializer.save(location=location)

            # ---------------- HANDLE BULK IMAGES ----------------
            images = data.getlist("images") if hasattr(data, "getlist") else data.get("images", [])
            image_objs = []

            for idx, img_data in enumerate(images):
                if not img_data:
                    continue
                # If img_data is a file or URL, append to list
                image_objs.append(
                    PropertyImage(
                        property=property_instance,
                        image_url=img_data,
                        display_order=idx + 1
                    )
                )

            if image_objs:
                PropertyImage.objects.bulk_create(image_objs)

            # ---------------- RESPONSE ----------------
            response_data = self.get_serializer(property_instance).data
            # Include created images in response
            response_data["images"] = PropertyImageSerializer(
                property_instance.property_img.order_by("display_order"), many=True
            ).data

            return Response(response_data)
             