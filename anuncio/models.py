from django.db import models

class Anuncio(models.Model):
    Cliente = models.CharField(max_length=100)
    Titulo = models.CharField(max_length=200)
    Preço = models.DecimalField(max_digits=5, decimal_places=2)
    Texto_Anuncio = models.CharField(max_length=1000)
    Nome_do_Contato = models.CharField(max_length=50)
    Telefone = models.CharField(max_length=200)
    secao = models.CharField(max_length=50)
    Tipo_de_Anuncio = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.Cliente
    
    
# Create your models here.
