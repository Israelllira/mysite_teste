from django.contrib import admin

from .models import *

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Matricula', 'Data_nascimento')

class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('Data_devolucao', 'Data_retirada', 'Aluno', 'Devolvido')
    filter_horizontal = ['livros']

admin.site.register(Livro)
admin.site.register(Autor)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)
    
# Register your models here.
