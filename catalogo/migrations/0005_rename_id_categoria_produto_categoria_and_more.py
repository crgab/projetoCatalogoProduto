# Generated by Django 5.2.3 on 2025-06-12 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0004_alter_produto_descricao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='id_categoria',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='produtofornecedor',
            old_name='id_fornecedor',
            new_name='fornecedor',
        ),
        migrations.RenameField(
            model_name='produtofornecedor',
            old_name='id_produto',
            new_name='produto',
        ),
    ]
