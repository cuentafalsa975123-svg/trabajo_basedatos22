from rest_framework import serializers
from .models import Interes

class InteresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interes
        fields = '__all__'  # O especifica los campos: ['id', 'nombre', 'categoria', ...]