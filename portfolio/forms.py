from django import forms
from .models import Projeto, Disciplina

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'conceitos', 'tecnologias', 'image', 'linkVideo', 'linkGit', 'linguagemProgramacao']


class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['curricularUnitName', 'curricularYear', 'semester', 'ects', 'curricularIUnitReadableCode', 'areaCientifica']
