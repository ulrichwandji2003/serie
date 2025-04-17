from django.db import models

# Create your models here.

class Reservation(models.Model):
    film = models.CharField(max_length=100)
    nombre_places = models.IntegerField()
    prix_total = models.DecimalField(max_digits=6, decimal_places=2)
    date_reservation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.film} - {self.nombre_places} places"
    
class Tiquet(models.Model):
    nom = models.CharField(max_length=100)
    film = models.CharField(max_length=100)
    salle = models.CharField(max_length=50)
    tel = models.CharField(max_length=20)
    date_diffusion = models.CharField(max_length=20)
    email_reception = models.EmailField()

    def __str__(self):
        return self.nom
    

from django.db import models

class Avis(models.Model):
    nom = models.CharField(max_length=100)  # Nom du visiteur
    commentaire = models.TextField()  # Texte de l'avis
    note = models.PositiveIntegerField()  # Note sur 5
    date = models.DateTimeField(auto_now_add=True)  # Date de soumission

    def __str__(self):
        return f"{self.nom} - {self.note}/5"