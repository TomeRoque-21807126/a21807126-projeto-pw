from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import ProjetoForm, DisciplinaForm

# Create your views here.

def index_view(request):
    curso = Curso.objects.first()
    context = {
        'curso': curso,
    }
    return render(request, "portfolio/index.html", context)

def disciplina_view(request, idDisc):
    disc = Disciplina.objects.get(curricularIUnitReadableCode=idDisc)
    context = {
        'disc': disc,
    }
    return render(request, "portfolio/disciplina.html", context)

def disciplinalist_view(request):
    discs = Disciplina.objects.all()
    context = {
        'discs': discs,
    }
    return render(request, "portfolio/disciplinalist.html", context)

def projetolist_view(request):
    context = {
        'proj': Projeto.objects.all(),
    }
    return render(request, "portfolio/projetolist.html", context)


def projeto_view(request, nome_proj):
    context = {
        'proj': Projeto.objects.get(nome=nome_proj),
    }
    return render(request, "portfolio/projeto.html", context)

def criar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('https://a21807126.pythonanywhere.com/portfolio/projetolist/')
    else:
        form = ProjetoForm()
    return render(request, 'portfolio/criar_form.html', {'form': form})

def editar_projeto(request, projeto_nome):
    projeto = get_object_or_404(Projeto, nome=projeto_nome)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('https://a21807126.pythonanywhere.com/portfolio/projetolist/')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'portfolio/editar_form.html', {'form': form})


def editar_disciplina(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, curricularIUnitReadableCode=disciplina_id)
    if request.method == 'POST':
        form = DisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('https://a21807126.pythonanywhere.com/portfolio/disciplinalist/')
    else:
        form = DisciplinaForm(instance=disciplina)
    return render(request, 'portfolio/editar_disc.html', {'form': form})

def criar_disciplina(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('https://a21807126.pythonanywhere.com/portfolio/disciplinalist/')
    else:
        form = DisciplinaForm()
    return render(request, 'portfolio/criar_disc.html', {'form': form})