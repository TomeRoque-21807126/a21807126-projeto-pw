from django.db import models

# Create your models here.

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='bandas/fotos/', blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    pais_origem = models.CharField(max_length=50, blank=True, null=True)
    genero = models.CharField(max_length=50, blank=True, null=True)
    data_formacao = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Album(models.Model):
    banda = models.ForeignKey(Banda, related_name='albuns', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    capa = models.ImageField(upload_to='albuns/capas/', blank=True, null=True)
    data_lancamento = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=50, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.banda.nome}"

class Musica(models.Model):
    album = models.ForeignKey(Album, related_name='musicas', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    duracao = models.DurationField(blank=True, null=True)
    spotify_link = models.URLField(max_length=200, blank=True, null=True)
    letra = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.album.titulo}"