from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Count
from .models import PropertyImage
from .serializers import propertyImageSerializer

class propertyImageViewSet(viewsets.ModelViewSet):
    queryset = PropertyImage.objects.all()
    serializer_class = propertyImageSerializer
     
    def get_queryset(self):         
        queryset = PropertyImage.objects.all()
        
        return queryset           

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        patient = serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
      