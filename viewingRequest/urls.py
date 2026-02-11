from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ViewingRequestViewSet

router = DefaultRouter()
router.register(r'', ViewingRequestViewSet, basename='viewingRequest')

urlpatterns = router.urls                              