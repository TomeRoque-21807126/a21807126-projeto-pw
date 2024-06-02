from django.urls import path
from . import views

app_name = 'artigos'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('post/<int:post_id>/', views.post_view, name='post'),
    path('editar/<str:item_type>/<int:item_id>/', views.edit_item, name='editar_form'),
    path('criar/<str:item_type>/', views.create_item, name='criar_form'),
]