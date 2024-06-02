# script_importacao.py

from portfolio.models import *
import json

def importar_dados(path):

    Curso.objects.all().delete()
    AreaCientifica.objects.all().delete()
    Disciplina.objects.all().delete()
    LinguagemProgramacao.objects.all().delete()
    Projeto.objects.all().delete()
    Docente.objects.all().delete()
    
    with open(path) as f:
        data = json.load(f)
    
        data_curso = data['courseDetail']
        
        Curso.objects.create(
            presentation = data_curso['presentation'],
            objectives = data_curso['objectives'],
            competences = data_curso['competences']
        )
        
        AreaCientifica.objects.create(
            nome = data_curso['scientificArea']
        )
    
        data_disc = data['courseFlatPlan']
        for info in data_disc: 
            Disciplina.objects.create(
                curricularUnitName = info['curricularUnitName'],
                curricularYear = info['curricularYear'],
                semester = info['semester'],
                ects = info['ects'],
                curricularIUnitReadableCode = info['curricularIUnitReadableCode'],
                areaCientifica = AreaCientifica.objects.get(nome="Informática")
            )