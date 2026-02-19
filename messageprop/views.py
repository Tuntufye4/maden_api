# views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import MessageProp
from .serializers import MessagePropSerializer

class MessagePropViewSet(viewsets.ModelViewSet):
    queryset = MessageProp.objects.all()
    serializer_class = MessagePropSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
              