from django.db import models
from django.utils import timezone

from django.contrib import admin


class LocalEvento(models.Model):
        class Meta:
                verbose_name_plural = "Local Evento"
                
        descricao = models.TextField('Descrição')

        def __str__(self):
            return self.descricao
        
class ItemAgenda(models.Model):
    data = models.DateField('Data do evento')
    hora = models.TimeField()
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição')
    criado_em = models.DateTimeField(auto_now_add=True)
    local = models.ForeignKey(LocalEvento, on_delete=models.CASCADE)
    participantes = models.ManyToManyField('auth.User')

        
    def __str__(self):
        return '{} {} - {}'.format(
            self.data.strftime('%d/%m/%y'),
            self.hora.strftime('%H:%M'),
            self.titulo)
    
    def criado_recente(self, obj):
        return obj.criado_em >= now() - timedelta(minutes=30)

    class Meta:
        verbose_name_plural = 'Tarefas agendadas'
        verbose_name = 'Tarefa agendada'
        ordering = ('-data', 'hora')

        
# Create your models here.
