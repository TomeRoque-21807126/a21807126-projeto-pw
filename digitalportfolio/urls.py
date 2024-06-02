from django.urls import path
from . import views

app_name = 'digitalportfolio'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('aboutme/', views.about_view, name='aboutme'),
]