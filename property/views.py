from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import transaction
from .models import Property
from .serializers import PropertySerializer
from propertyImage.models import PropertyImage
from propertyImage.serializers import PropertyImageSerializer
from location.models import Location

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        try:
            with transaction.atomic():
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

                # ---------------- CREATE PROPERTY ----------------
                serializer = self.get_serializer(data=data)
                if not serializer.is_valid():
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                property_instance = serializer.save(location=location)

                # ---------------- HANDLE BULK IMAGES ----------------
                images = data.getlist("images") if hasattr(data, "getlist") else data.get("images") or []
                image_objs = []

                for idx, img_data in enumerate(images):
                    if not img_data:
                        continue
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
                response_data["images"] = PropertyImageSerializer(
                    property_instance.property_img.order_by("display_order"), many=True               
                ).data

                return Response(response_data, status=status.HTTP_201_CREATED)

        except Exception as e:
            # Catch unexpected errors and return 400
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
