from django.db import models

# Create your models here.

class Streaming(models.Model):
    Nom_streaming = models.CharField(max_length=255,)
    Description = models.CharField(max_length=255,)
    Genre = models.CharField(max_length=255, default="Science-fiction | Drame | Action")
    Realisateur = models.CharField(max_length=50)
    Acteurs = models.CharField(max_length=50)
    Duree_streaming = models.CharField(max_length=50)
    Note = models.CharField(max_length=50)
    Date_streaming = models.DateField(blank=True, null=True)
    Type_streaming = models.CharField(max_length=50, default="film")
    Image_streaming = models.ImageField(upload_to='Telechargement')
    Video_streaming = models.FileField(upload_to='Telechargement')
    Prix_streaming = models.IntegerField()
    Salle_streaming = models.CharField(max_length=50)


    def __str__(self):
        return self.Nom_streaming
    

class Contact(models.Model):
    Nom = models.CharField(max_length=50)
    Email = models.EmailField(max_length=55)
    Message = models.TextField(max_length=255)

    def __str__(self):
        return self.Nom