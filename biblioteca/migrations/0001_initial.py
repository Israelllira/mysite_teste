# Generated by Django 2.2.4 on 2019-09-22 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Matricula', models.CharField(max_length=12, unique=True)),
                ('Nome', models.CharField(max_length=50)),
                ('Data_nascimento', models.DateField()),
                ('Email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=50)),
                ('Sobrenome', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=100)),
                ('Ano_publicacao', models.IntegerField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Autor')),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data_retirada', models.DateField()),
                ('Data_devolucao', models.DateField()),
                ('Devolvido', models.BooleanField()),
                ('Aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Aluno')),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('livros', models.ManyToManyField(to='biblioteca.Livro')),
            ],
        ),
    ]
