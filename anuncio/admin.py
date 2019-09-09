from django.contrib import admin

from .models import Anuncio

class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('Cliente', 'Preço', 'Telefone')

admin.site.register(Anuncio, AnuncioAdmin)
    
# Register your models here.
