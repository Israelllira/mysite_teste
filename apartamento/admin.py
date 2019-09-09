from django.contrib import admin

from .models import Apartamento

class ApartamentoAdmin(admin.ModelAdmin):
    list_display = ('Numero', 'Valor_Condominio', 'Qtd_Quartos')

admin.site.register(Apartamento, ApartamentoAdmin)
    
# Register your models here.
