from django.db import models

# Create your models here.

class Banda(models.Model):
    nome = models.CharField(max_length = 100)

class Festival(models.Model):
    nome = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='festival_images/', blank=True, null=True)
    link = models.URLField(blank=True)
    bandas = models.ManyToManyField(Banda)

class Localizacao(models.Model):
    nome = models.CharField(max_length = 100)
    festivais = models.ManyToManyField(Festival)

