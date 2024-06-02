from django.db import models

# Create your models here.
class Curso(models.Model):
    presentation = models.CharField(max_length = 200)
    objectives = models.CharField(max_length = 100)
    competences = models.CharField(max_length = 100)

class AreaCientifica(models.Model):
    nome = models.CharField(max_length = 100)

class Disciplina(models.Model):
    curricularUnitName = models.CharField(max_length = 100)
    curricularYear = models.IntegerField(max_length = 4)
    semester = models.CharField(max_length = 14)
    ects = models.IntegerField(max_length = 1)
    curricularIUnitReadableCode = models.CharField(max_length = 13)
    areaCientifica = models.ForeignKey(AreaCientifica, on_delete=models.CASCADE)

class LinguagemProgramacao(models.Model):
    nome = models.CharField(max_length = 100)

class Projeto(models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.CharField(max_length = 300)
    conceitos = models.CharField(max_length = 200)
    tecnologias = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='disciplina_images/', blank=True, null=True)
    linkVideo = models.URLField(blank=True)
    linkGit = models.URLField(blank=True)
    linguagemProgramacao = models.ManyToManyField(LinguagemProgramacao)

class Docente(models.Model):
    nome = models.CharField(max_length = 100)
    disciplinas = models.ManyToManyField(Disciplina)





