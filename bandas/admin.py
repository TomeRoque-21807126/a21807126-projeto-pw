from django.contrib import admin
from .models import Banda, Album, Musica

# Register your models here.

class BandaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'genero', 'data_formacao')
    search_fields = ('nome', 'genero')
    list_filter = ('pais_origem', 'genero')

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'banda', 'genero')
    search_fields = ('titulo', 'banda__nome', 'genero')
    list_filter = ('data_lancamento', 'genero')

class MusicaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'album', 'duracao', 'spotify_link')
    search_fields = ('titulo', 'album__titulo')
    list_filter = ('album',)

admin.site.register(Banda, BandaAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Musica, MusicaAdmin)
