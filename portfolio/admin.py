from django.contrib import admin
from django.utils.html import format_html
from .models import Curso, AreaCientifica, Disciplina, Projeto, LinguagemProgramacao, Docente

# Register your models here.

class CursoAdmin(admin.ModelAdmin):
    list_display = ('presentation', 'objectives', 'competences')
    search_fields = ('objectives','competences')

admin.site.register(Curso, CursoAdmin)

'''
class AreaCientificaAdmin(admin.ModelAdmin):
    list_display = ('nome')
    ordering = ('nome')
    search_field = ('nome')

admin.site.register(AreaCientifica, AreaCientificaAdmin)
'''
admin.site.register(AreaCientifica)

class DisciplinaAdmin(admin.ModelAdmin):
    list_display =('curricularUnitName', 'curricularYear', 'semester', 'ects', 'curricularIUnitReadableCode', 'areaCientifica')
    ordering = ('curricularYear', 'semester', 'ects')
    search_field = ('curricularUnitName', 'curricularYear', 'semester')

admin.site.register(Disciplina, DisciplinaAdmin)

class ProjetoAdmin(admin.ModelAdmin):
    list_display =('nome', 'descricao', 'conceitos', 'tecnologias', 'image', 'linkVideo', 'linkGit')
    ordering = ('nome', 'conceitos', 'tecnologias')
    search_field = ('nome', 'conceitos', 'tecnologias')

admin.site.register(Projeto, ProjetoAdmin)

'''
class LinguagemProgramacaoAdmin(admin.ModelAdmin):
    list_display =('nome')
    ordering = ('nome')
    search_field = ('nome')

admin.site.register(LinguagemProgramacao, LinguagemProgramacaoAdmin)
'''
admin.site.register(LinguagemProgramacao)

'''
class DocenteAdmin(admin.ModelAdmin):
    list_display =('nome', 'disciplinas')
    ordering = ('nome')
    search_field = ('nome')

admin.site.register(Docente, DocenteAdmin)
'''
admin.site.register(Docente)
