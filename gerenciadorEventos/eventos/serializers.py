from rest_framework import serializers
from .models import Eventos

class EventosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventos  # Substitua pelo nome correto do seu modelo
        fields = '__all__'  # Ou defina os campos específicos
