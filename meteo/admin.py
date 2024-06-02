from django.contrib import admin
from .models import Cidade, Previsao

# Register your models here.

admin.site.register(Cidade)
admin.site.register(Previsao)