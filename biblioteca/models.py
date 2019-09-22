from django.db import models

class Autor(models.Model):
        class Meta:
                verbose_name_plural = "Autores"
                
        Nome = models.CharField(max_length=50)
        Sobrenome = models.CharField(max_length=50)

        def __str__(self):
            return self.Sobrenome.upper() + ', ' + self.Nome

class Aluno(models.Model):
        Matricula = models.CharField(max_length=12, unique=True)
        Nome = models.CharField(max_length=50)
        Data_nascimento = models.DateField()
        Email = models.EmailField(max_length=100)

        def __str__(self):
            return self.Nome

class Livro(models.Model):
        Titulo = models.CharField(max_length=100)
        Autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
        Ano_publicacao = models.IntegerField()

        def __str__(self):
            return "{}, ({})".format(self.Titulo, self.Ano_publicacao)

class Emprestimo(models.Model):
        Usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
        Aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE) 
        Data_retirada = models.DateField()
        Data_devolucao = models.DateField()
        livros = models.ManyToManyField(Livro)
        Devolvido = models.BooleanField()

        def __str__(self):
            return "{}, ({})".format(self.Aluno, self.Usuario)
        

# Create your models here.
