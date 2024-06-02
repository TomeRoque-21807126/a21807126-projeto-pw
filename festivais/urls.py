# festivais/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'festivais'
urlpatterns = [
    path('', views.festivais_view, name='festivais'),
    path('festival/<str:nome_fest>/', views.festival_view, name = "festival"),
]