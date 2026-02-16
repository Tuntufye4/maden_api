from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import PropertyImage
from .serializers import PropertyImageSerializer


class PropertyImageViewSet(viewsets.ModelViewSet):
    """
    CRUD for Property Images.
    """
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        # Avoid duplicates: same property + display_order
        property_image, created = PropertyImage.objects.get_or_create(
            property=validated_data.get("property"),
            display_order=validated_data.get("display_order"),
            defaults={"image_url": validated_data.get("image_url")},
        )

        return Response(
            PropertyImageSerializer(property_image).data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )
            