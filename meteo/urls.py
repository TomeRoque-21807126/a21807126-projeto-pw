# meteo/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'meteo'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('prevList/', views.prevlist_view, name='prevList'),
]