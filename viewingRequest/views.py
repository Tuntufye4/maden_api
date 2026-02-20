from rest_framework import viewsets, permissions
from .models import ViewingRequest
from .serializers import ViewingRequestSerializer

class ViewingRequestViewSet(viewsets.ModelViewSet):
    serializer_class = ViewingRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Users see only their own requests
        #user = self.request.user
        #return ViewingRequest.objects.all().order_by('-created_at')
        return ViewingRequest.objects.all().order_by('-created_at')   

    def perform_create(self, serializer):
        # Auto-attach the logged-in user
        serializer.save(user=self.request.user)
     