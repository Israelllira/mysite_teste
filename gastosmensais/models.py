from django.db import models
from django.utils import timezone
from django.contrib import admin


class TipoDespesa(models.Model):
        class Meta:
                verbose_name_plural = "Tipo de Despesa"
                
        despesa = models.CharField('Despesa', max_length=20)

        def __str__(self):
            return self.despesa

class FormaPagamento(models.Model):
        class Meta:
                verbose_name_plural = "Forma de Pagamento"
                
        pagamento = models.CharField('Forma de Pagamento', max_length=20)

        def __str__(self):
            return self.pagamento
        
class ItemGasto(models.Model):
    data = models.DateField('Data do Gasto')
    despesa = models.ForeignKey(TipoDespesa, on_delete=models.CASCADE)
    descricao = models.TextField('Descrição')
    pagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)
    vencimento = models.DateField('Vencimento')
    quitado = models.BooleanField()

        
    
    def vecndias(self, obj):
        return obj.vencimento == -2
    
    class Meta:
        verbose_name_plural = 'Gastos Mensais'
        verbose_name = 'Gasto Mensal'
        ordering = ('-vencimento', 'pagamento')

        
# Create your models here.
