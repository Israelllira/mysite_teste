# Generated by Django 2.2.4 on 2019-09-22 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livro',
            old_name='autor',
            new_name='Autor',
        ),
    ]