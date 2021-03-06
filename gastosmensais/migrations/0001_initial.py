# Generated by Django 2.2.4 on 2019-10-26 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormaPagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagamento', models.CharField(max_length=20, verbose_name='Forma de Pagamento')),
            ],
            options={
                'verbose_name_plural': 'Forma de Pagamento',
            },
        ),
        migrations.CreateModel(
            name='TipoDespesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('despesa', models.CharField(max_length=20, verbose_name='Despesa')),
            ],
            options={
                'verbose_name_plural': 'Tipo de Despesa',
            },
        ),
        migrations.CreateModel(
            name='ItemGasto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data do Gasto')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('vencimento', models.DateField(verbose_name='Vencimento')),
                ('quitado', models.BooleanField()),
                ('despesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gastosmensais.TipoDespesa')),
                ('pagamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gastosmensais.FormaPagamento')),
            ],
            options={
                'verbose_name': 'Gasto Mensal',
                'verbose_name_plural': 'Gastos Mensais',
                'ordering': ('-vencimento', 'pagamento'),
            },
        ),
    ]
