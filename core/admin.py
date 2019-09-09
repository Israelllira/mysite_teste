from django.contrib import admin

from .models import Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')

admin.site.register(Contato, ContatoAdmin)
    
# Register your models here.
