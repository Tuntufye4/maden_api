from rest_framework import viewsets, permissions
from .models import RentContract
from .serializers import HouseContractSerializer
    
class HouseContractViewSet(viewsets.ModelViewSet):
    serializer_class = HouseContractSerializer   
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Users see only their own requests
        #user = self.request.user
        #return ViewingRequest.objects.all().order_by('-created_at')
        return RentContract.objects.all().order_by('-created_at')   

    def perform_create(self, serializer):
        # Auto-attach the logged-in user
        serializer.save(user=self.request.user)
             