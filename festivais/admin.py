from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register your models here.

admin.site.register(Festival)

admin.site.register(Localizacao)

admin.site.register(Banda)
