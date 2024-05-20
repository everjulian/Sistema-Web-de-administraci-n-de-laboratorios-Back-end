from rest_framework import serializers
from .models import ActivosModel

class ActivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivosModel
        fields = '__all__'
