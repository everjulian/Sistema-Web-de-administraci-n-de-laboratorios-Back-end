from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivoViewSet

router = DefaultRouter()
router.register(r'activos', ActivoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
