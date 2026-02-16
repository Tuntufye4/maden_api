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

    # Optional: override create to avoid duplicates by country/region/city/area
    def create(self, request, *args, **kwargs):    
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        location, created = Location.objects.get_or_create(
          #  country=data.get('country').strip(),
            region=data.get('region').strip(),   
            city=data.get('city').strip(),
            area=data.get('area').strip(),
            defaults={   
                'created_at': data.get('created_at'),
            }
        )

        return Response(LocationSerializer(location).data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
             