from django.db import models

class Compras(models.Model):
    Nome = models.CharField(max_length=100)
    Descrição_Produto = models.CharField(max_length=300)
    Unidade_Compra = models.CharField(max_length=300)
    Data_Compra = models.DateField()
    Valor = models.FloatField()
    Preço_Maximo = models.FloatField()

    def Preço_Maximo(self):
        return self.Valor
    
# Create your models here.
