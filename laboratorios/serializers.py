from rest_framework import serializers
from .models import LaboratoriosModel

class LaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaboratoriosModel
        fields = '__all__'
