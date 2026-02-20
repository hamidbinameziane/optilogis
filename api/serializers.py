from rest_framework import serializers
from .models import Client, Intervention

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class InterventionSerializer(serializers.ModelSerializer):
    # Ce champ sera utilisé par Flutter pour LIRE l'URL propre
    imageUrl = serializers.SerializerMethodField()

    class Meta:
        model = Intervention
        # 'image' est le champ brut (pour l'upload)
        # 'imageUrl' est le champ formaté (pour l'affichage Flutter)
        fields = ['id', 'title', 'description', 'status', 'image', 'imageUrl']
        # On rend 'image' invisible à la lecture mais disponible à l'écriture
        extra_kwargs = {'image': {'write_only': True}}

    def get_imageUrl(self, obj):
        if obj.image:
            # On récupère l'URL Cloudinary et on force le HTTPS
            url = obj.image.url
            return url.replace('http://', 'https://')
        return None
        