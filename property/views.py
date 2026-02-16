from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Property
from .serializers import PropertySerializer


class PropertyViewSet(viewsets.ModelViewSet):
    """
    CRUD for Properties.
    Supports multipart uploads + image upload.
    """
    queryset = Property.objects.all().order_by("-created_at")
    serializer_class = PropertySerializer
    parser_classes = (MultiPartParser, FormParser)

    # ---------- HELPER ----------
    def handle_images(self, instance, request):
        images = request.FILES.getlist("images")
        if images:
            instance.image_url = images[0]  # store first image only
            instance.display_order = "1"
            instance.save()

    # ---------------- CREATE ----------------
    def create(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                data = request.data.copy()
                data.pop("images", None)

                serializer = self.get_serializer(data=data)
                serializer.is_valid(raise_exception=True)

                instance = serializer.save()
                self.handle_images(instance, request)

                return Response(
                    PropertySerializer(instance, context={"request": request}).data,
                    status=status.HTTP_201_CREATED,
                )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    # ---------------- UPDATE ----------------
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data.copy()
        data.pop("images", None)

        serializer = self.get_serializer(instance, data=data)
        serializer.is_valid(raise_exception=True)

        instance = serializer.save()
        self.handle_images(instance, request)

        return Response(
            PropertySerializer(instance, context={"request": request}).data   
        )

    # ---------------- PATCH ----------------
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data.copy()
        data.pop("images", None)

        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)

        instance = serializer.save()
        self.handle_images(instance, request)

        return Response(   
            PropertySerializer(instance, context={"request": request}).data
        )
        