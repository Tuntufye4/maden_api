# property/views.py
from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Property
from .serializers import PropertySerializer

class PropertyViewSet(viewsets.ModelViewSet):
    """
    CRUD for Property with single image upload.
    """
    queryset = Property.objects.all().order_by("-created_at")
    serializer_class = PropertySerializer
    parser_classes = (MultiPartParser, FormParser)   

    def save_property(self, instance=None, partial=False):
        data = self.request.data.copy()
        if "images" in data:  # support legacy 'images' key
            data["image"] = self.request.FILES.getlist("images")[0]
        elif "image" in self.request.FILES:
            data["image"] = self.request.FILES["image"]

        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        return serializer.save()

    def create(self, request, *args, **kwargs):  
        try:
            with transaction.atomic():
                instance = self.save_property()
                return Response(
                    PropertySerializer(instance, context={"request": request}).data,
                    status=status.HTTP_201_CREATED
                )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        with transaction.atomic():
            instance = self.save_property(instance)
        return Response(PropertySerializer(instance, context={"request": request}).data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        with transaction.atomic():
            instance = self.save_property(instance, partial=True)
        return Response(PropertySerializer(instance, context={"request": request}).data)
