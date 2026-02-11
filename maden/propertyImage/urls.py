from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import propertyImageViewSet

router = DefaultRouter()
router.register(r'', propertyImageViewSet, basename='propertyImage')

urlpatterns = router.urls                            