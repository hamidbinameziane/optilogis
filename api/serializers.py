from rest_framework import serializers
from .models import Client, Intervention

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class InterventionSerializer(serializers.ModelSerializer):
    # On crée un champ virtuel pour l'URL propre que Flutter va lire
    imageUrl = serializers.SerializerMethodField()

    class Meta:
        model = Intervention
        # 'image' est le champ réel du modèle (pour l'upload)
        # 'imageUrl' est le champ calculé (pour l'affichage)
        fields = ['id', 'title', 'description', 'status', 'image', 'imageUrl']
        
        # On dit à Django que 'image' sert à l'écriture (upload) 
        # mais qu'on ne veut pas le voir dans le JSON de réponse
        extra_kwargs = {
            'image': {'write_only': True}
        }

    # Cette méthode DOIT s'appeler get_<nom_du_champ>
    def get_imageUrl(self, obj):
        if obj.image:
            # On récupère l'URL de Cloudinary et on sécurise en HTTPS
            return obj.image.url.replace('http://', 'https://')
        return None
        