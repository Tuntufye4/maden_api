from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Property, Location
from .serializers import PropertySerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def get_queryset(self):
        # Optional: filter by query params later
        queryset = Property.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
         
        # Handle location
       # country = data.pop("country", None)
        region = data.pop("region", None)
        city = data.pop("city", None)
        area = data.pop("area", None)

        location = None
        if region and city and area:
            location, _ = Location.objects.get_or_create(     
             #   country=country.strip(),
                region=region.strip(),   
                city=city.strip(),
                area=area.strip(),    
                defaults={}
            )
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        property_instance = serializer.save(location=location)

        return Response(self.get_serializer(property_instance).data, status=status.HTTP_201_CREATED)
     