from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessagePropViewSet

router = DefaultRouter()
router.register(r'', MessagePropViewSet, basename='messageprop')

urlpatterns = router.urls                                             