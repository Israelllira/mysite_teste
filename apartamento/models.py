from django.db import models

class Apartamento(models.Model):
    Numero = models.IntegerField()
    Qtd_Quartos = models.IntegerField()
    Proprietario = models.CharField(max_length=100)
    Valor_Condominio = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.Proprietario
    
    
# Create your models here.
