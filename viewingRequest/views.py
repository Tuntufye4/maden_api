from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ViewingRequest
from .serializers import ViewingRequestSerializer

class ViewingRequestViewSet(viewsets.ModelViewSet):
    queryset = ViewingRequest.objects.all()
    serializer_class = ViewingRequestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically attach the logged-in user
        serializer.save(user=self.request.user)
         