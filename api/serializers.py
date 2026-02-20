from rest_framework import serializers
from .models import Client, Intervention

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class InterventionSerializer(serializers.ModelSerializer):
    # On crée un champ virtuel pour l'URL propre que Flutter va lire
    image = serializers.SerializerMethodField()

    class Meta:
        model = Intervention
        # 'image' est le champ réel du modèle (pour l'upload)
        # 'imageUrl' est le champ calculé (pour l'affichage)
        fields = '__all__'
        
        # On dit à Django que 'image' sert à l'écriture (upload) 
        # mais qu'on ne veut pas le voir dans le JSON de réponse

        