from django.contrib import admin

from .models import Compras

class ComprasAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Valor', 'Preço_Maximo')

admin.site.register(Compras, ComprasAdmin)
    
# Register your models here.
