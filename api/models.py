from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    adresse = models.TextField()

    def __str__(self):
        return self.nom

class Intervention(models.Model):
    STATUT_CHOICES = [
        ('A_FAIRE', 'À faire'),
        ('EN_COURS', 'En cours'),
        ('TERMINE', 'Terminé'),
    ]
    titre = models.CharField(max_length=200)
    description = models.TextField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='A_FAIRE')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    technicien = models.ForeignKey(User, on_delete=models.CASCADE, related_name='missions')
    image =CloudinaryField('image', folder='interventions', null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titre} - {self.statut}"
    

