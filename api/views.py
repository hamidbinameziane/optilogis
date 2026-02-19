from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from rest_framework import viewsets
from .models import Client, Intervention
from .serializers import ClientSerializer, InterventionSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class InterventionViewSet(viewsets.ModelViewSet):
    queryset = Intervention.objects.all()
    serializer_class = InterventionSerializer
    
class InterventionViewSet(viewsets.ModelViewSet):
    serializer_class = InterventionSerializer
    permission_classes = [IsAuthenticated] # Sécurité supplémentaire

    def get_queryset(self):
        # On récupère l'utilisateur qui fait la requête grâce au Token
        user = self.request.user
        
        # Si c'est l'admin, il voit tout
        if user.is_staff:
            return Intervention.objects.all()
        
        # Sinon, on ne renvoie que SES interventions
        return Intervention.objects.filter(technicien=user)
        
    def perform_create(self, serializer):
        # Enregistre l'intervention en forçant le technicien à être l'utilisateur connecté
        serializer.save(technicien=self.request.user)