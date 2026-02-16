from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Property
from location.models import Location
from propertyImage.models import PropertyImage
from .serializers import PropertySerializer
from propertyImage.serializers import PropertyImageSerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def get_queryset(self):
        return Property.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data.copy()

        # ---------------- HANDLE LOCATION ----------------
        region = data.pop("region", None)
        city = data.pop("city", None)
        area = data.pop("area", None)
        location = None

        if region and city and area:
            location, _ = Location.objects.get_or_create(
                region=region.strip(),
                city=city.strip(),
                area=area.strip()
            )

        # ---------------- CREATE PROPERTY + IMAGES ATOMICALLY ----------------
        with transaction.atomic():
            # Create Property
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            property_instance = serializer.save(location=location)

            # Handle Images
            images = data.getlist("images") if hasattr(data, "getlist") else data.get("images", [])
            created_images = []

            for idx, img_data in enumerate(images):
                # img_data can be a file or a URL
                img_serializer = PropertyImageSerializer(
                    data={
                        "property": property_instance.id,  # pass ID if serializer uses PrimaryKeyRelatedField
                        "image_url": img_data,
                        "display_order": idx + 1
                    }
                )
                if img_serializer.is_valid():
                    img_instance = img_serializer.save()
                    created_images.append(img_serializer.data)
                else:
                    # optionally log errors
                    print(f"Invalid image at index {idx}: {img_serializer.errors}")
                    continue

        # ---------------- RESPONSE ----------------
        response_data = self.get_serializer(property_instance).data
        response_data["images"] = created_images
        return Response(response_data, status=status.HTTP_201_CREATED)
          