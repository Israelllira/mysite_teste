from django.contrib import admin
from .models import *

from django.conf.locale.pt_BR import formats as pt_BR_formats

pt_BR_formats.DATETIME_FORMAT = "d M Y H:i"
pt_BR_formats.DATE_FORMAT = "d M Y"


class ItemAgendaAdmin(admin.ModelAdmin):
    list_display = ('data', 'hora', 'titulo', 'criado_em')
    date_hierarchy = ('data')
    search_fieldes = ('titulo',)
    filter_horizontal = ('participantes',)

        

class AuthorAdmin(admin.ModelAdmin):
    fields = ('name', 'title')
    
class AuthorAdmin(admin.ModelAdmin):
    exclude = ('birth_date')


admin.site.register(LocalEvento)
admin.site.register(ItemAgenda, ItemAgendaAdmin)
    
# Register your models here.
