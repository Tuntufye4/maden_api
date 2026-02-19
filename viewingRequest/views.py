from rest_framework import viewsets, permissions
from .models import ViewingRequest
from .serializers import ViewingRequestSerializer

class ViewingRequestViewSet(viewsets.ModelViewSet):
    queryset = ViewingRequest.objects.all().order_by('-created_at')
    serializer_class = ViewingRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Auto-attach the logged-in user
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Optional: users see only their own requests
        user = self.request.user
        return ViewingRequest.objects.filter(user=user).order_by('-created_at')
                  