# Generated by Django 5.2.3 on 2025-06-12 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_produto_imagem_alter_categoria_nome_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.CharField(db_column='descricao', default='', max_length=250),
        ),
    ]
