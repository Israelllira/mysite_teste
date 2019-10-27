from django.contrib import admin
from .models import *

from django.conf.locale.pt_BR import formats as pt_BR_formats

pt_BR_formats.DATETIME_FORMAT = "d M Y H:i"
pt_BR_formats.DATE_FORMAT = "d M Y"


class ItemGastoAdmin(admin.ModelAdmin):
    list_display = ('data', 'despesa', 'descricao', 'pagamento', 'vencimento', 'quitado', 'vecndias')
    date_hierarchy = ('vencimento')
    search_fieldes = ('vencimento', 'quitado')
    list_filter = ['vencimento', 'quitado']

    def vecndias(self, obj):
        return obj.vencimento == -2

    vecndias.short_description = 'vencendo em 2 dias?'
    vecndias.boolean = True
    
admin.site.register(TipoDespesa)
admin.site.register(FormaPagamento)
admin.site.register(ItemGasto, ItemGastoAdmin)
    
# Register your models here.
