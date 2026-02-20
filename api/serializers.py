from rest_framework import serializers
from .models import Client, Intervention

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class InterventionSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField() # On prend le contrôle du champ image

    class Meta:
        model = Intervention
        fields = '__all__'

    def get_image(self, obj):
        if obj.image:
            # On force l'URL en HTTPS pour Android
            return obj.image.url.replace('http://', 'https://')
        return None
        