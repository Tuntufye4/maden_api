from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Location
from .serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    """
    CRUD for Locations.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        # Avoid duplicates: same region + city + area
        location, created = Location.objects.get_or_create(
            region=validated_data.get("region").strip(),
            city=validated_data.get("city").strip(),
            area=validated_data.get("area").strip(),
            defaults={"created_at": validated_data.get("created_at")},
        )

        status_code = status.HTTP_201_CREATED if created else status.HTTP_200_OK
        return Response(LocationSerializer(location).data, status=status_code)
         