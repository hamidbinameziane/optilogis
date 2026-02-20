from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import cloudinary.uploader

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
    
# 1. Supprimer l'image de Cloudinary quand on supprime l'objet Intervention
@receiver(post_delete, sender=Intervention)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        cloudinary.uploader.destroy(instance.image.public_id)

# 2. Supprimer l'ancienne image quand on la remplace par une nouvelle
@receiver(pre_save, sender=Intervention)
def delete_old_image_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_image = Intervention.objects.get(pk=instance.pk).image
    except Intervention.DoesNotExist:
        return False

    new_image = instance.image
    if old_image and old_image != new_image:
        cloudinary.uploader.destroy(old_image.public_id)

