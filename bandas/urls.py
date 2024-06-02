from django.urls import path
from . import views

app_name = 'bandas'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('album/<int:album_id>/', views.album_view, name='album'),
    path('banda/<int:banda_id>/', views.banda_view, name='banda'),
    path('musica/<int:musica_id>/', views.musica_view, name='musica'),
    path('editar/<str:item_type>/<int:item_id>/', views.edit_item, name='editar_form'),
    path('criar/<str:item_type>/', views.create_item, name='criar_form'),
    path('html5css_view/', views.html5css_view, name='html5css'),

]
