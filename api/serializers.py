from rest_framework import serializers
from .models import Client, Intervention

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class InterventionSerializer(serializers.ModelSerializer):
    # On définit explicitement imageUrl comme une chaîne de caractères
    # read_only=True évite que Django cherche une méthode get_image
    imageUrl = serializers.ReadOnlyField(source='image.url', default=None)

    class Meta:
        model = Intervention
        # 'image' est pour l'upload depuis Flutter
        # 'imageUrl' est pour l'affichage dans Flutter
        fields = ['id', 'title', 'description', 'status', 'image', 'imageUrl']
        extra_kwargs = {
            'image': {'write_only': True}
        }

    # Pour corriger le problème du HTTPS sans créer de SerializerMethodField complexe
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation.get('imageUrl'):
            representation['imageUrl'] = representation['imageUrl'].replace('http://', 'https://')
        return representation
        