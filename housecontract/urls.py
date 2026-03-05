from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HouseContractViewSet

router = DefaultRouter()
router.register(r'', HouseContractViewSet, basename='rentContract')             

urlpatterns = router.urls      