from rest_framework import serializers
from .models import MarcasModel

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarcasModel
        fields = '__all__'
