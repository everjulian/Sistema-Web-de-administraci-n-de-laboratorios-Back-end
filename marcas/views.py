from rest_framework import viewsets
from .models import MarcasModel
from .serializers import MarcaSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = MarcasModel.objects.all()
    serializer_class = MarcaSerializer
