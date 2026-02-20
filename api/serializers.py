from rest_framework import serializers
from .models import Client, Intervention

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class InterventionSerializer(serializers.ModelSerializer):
    # Ce champ sera utilisé par Flutter pour LIRE l'URL propre
    image = serializers.SerializerMethodField()

    class Meta:
        model = Intervention
        fields = '__all__'
        