from rest_framework import viewsets
from .models import LaboratoriosModel
from .serializers import LaboratorioSerializer

class LaboratorioViewSet(viewsets.ModelViewSet):
    queryset = LaboratoriosModel.objects.all()
    serializer_class = LaboratorioSerializer
