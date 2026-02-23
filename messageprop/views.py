# views.py

from .models import MessageProp
from .serializers import MessagePropSerializer
from rest_framework import viewsets, permissions

class MessagePropViewSet(viewsets.ModelViewSet):
    """
    ViewSet for MessageProp.
    Returns all messages for authenticated users.
    """
    serializer_class = MessagePropSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return all messages, ordered by newest first
        return MessageProp.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        # Save message with the logged-in user
        serializer.save(user=self.request.user)    