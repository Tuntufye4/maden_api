from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyImageViewSet

router = DefaultRouter()
router.register(r'', PropertyImageViewSet, basename='propertyImage')

urlpatterns = router.urls                              