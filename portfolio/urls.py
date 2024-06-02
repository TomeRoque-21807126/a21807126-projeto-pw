# portfolio/urls.py

from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.index_view, name = "home"),
    path('disciplina/<str:idDisc>/', views.disciplina_view, name='disciplina'),
    path('disciplinalist/', views.disciplinalist_view, name='disciplinalist'),
    path('projetolist/', views.projetolist_view, name = "projetolist"),
    path('projeto/<str:nome_proj>/', views.projeto_view, name = "projeto"),
    path('projeto/<str:nome_proj>/', views.projeto_view, name = "projeto"),
    path('criar/', views.criar_projeto, name='criar_projeto'),
    path('editar/<str:projeto_nome>/', views.editar_projeto, name='editar_projeto'),
    path('criarDisc/', views.criar_disciplina, name='criar_disciplina'),
    path('editarDisc/<str:disciplina_id>/', views.editar_disciplina, name='editar_disciplina'),
]