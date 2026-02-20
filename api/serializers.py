from rest_framework import serializers
from .models import Client, Intervention

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class InterventionSerializer(serializers.ModelSerializer):
    # Champ virtuel pour l'URL sécurisée Cloudinary
    imageUrl = serializers.ReadOnlyField(source='image.url', default=None)

    class Meta:
        model = Intervention
        # On utilise les noms EXACTS de ton modèle : titre, statut, etc.
        fields = [
            'id', 
            'titre', 
            'description', 
            'statut', 
            'client', 
            'technicien', 
            'image',     # Pour l'upload (écriture seule)
            'imageUrl',  # Pour l'affichage (lecture seule)
            'date_creation'
        ]
        extra_kwargs = {
            'image': {'write_only': True}
        }

    # Force le HTTPS pour l'affichage sur Android
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation.get('imageUrl'):
            representation['imageUrl'] = representation['imageUrl'].replace('http://', 'https://')
        return representation
    