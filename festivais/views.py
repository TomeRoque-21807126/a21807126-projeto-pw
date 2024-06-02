from django.shortcuts import render
from .models import *

# Create your views here.

def festivais_view(request):
    locals = Localizacao.objects.all()
    context = {
        'locals': locals,
    }
    return render(request, "festivais/festivais.html", context)

def festival_view(request, nome_fest):
    fest = Festival.objects.get(nome=nome_fest)
    context = {
        'fest': fest,
    }
    return render(request, "festivais/festival.html", context)