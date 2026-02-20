# views.py

from .models import MessageProp
from .serializers import MessagePropSerializer

from rest_framework import viewsets, permissions

class MessagePropViewSet(viewsets.ModelViewSet):
    serializer_class = MessagePropSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Optional: only messages by the logged-in user
        return MessageProp.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)    