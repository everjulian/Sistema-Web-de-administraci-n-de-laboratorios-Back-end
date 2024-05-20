from rest_framework import viewsets
from .models import ActivosModel
from .serializers import ActivoSerializer

class ActivoViewSet(viewsets.ModelViewSet):
    queryset = ActivosModel.objects.all()
    serializer_class = ActivoSerializer
