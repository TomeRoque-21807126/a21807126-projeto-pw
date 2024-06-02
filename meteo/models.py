from django.db import models

# Create your models here.

class Cidade(models.Model):
    name = models.CharField(max_length=100)

class Previsao(models.Model):
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    data = models.DateField()
    temp_min = models.DecimalField(max_digits=5, decimal_places=2)
    temp_max = models.DecimalField(max_digits=5, decimal_places=2)
    previsoes = models.ForeignKey('self', on_delete=models.CASCADE, related_name='prevs', null=True, blank=True)
    wtid = models.CharField(max_length=2, null=True, blank=True)