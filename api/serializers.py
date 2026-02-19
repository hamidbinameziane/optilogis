from rest_framework import serializers
from .models import Client, Intervention

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class InterventionSerializer(serializers.ModelSerializer):
    client_nom = serializers.ReadOnlyField(source='client.nom') # Pour Flutter
    class Meta:
        model = Intervention
        fields = '__all__'
        