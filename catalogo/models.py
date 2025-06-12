from django.db import models
from django.db.models.fields import CharField


class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True
    )

    class Meta:
        abstract = True
        managed = True


class Categoria(models.Model):
    nome_categoria = models.CharField(
        db_column='nome_categoria',
        null=False,
        default='',
        max_length=70
    )

    def __str__(self):
        return f"{self.id} - {self.nome_categoria}:"


class Produto(ModelBase):
    descricao = models.CharField(
        db_column='descricao',
        null=False,
        default='',
        max_length=250
    )
    marca = models.CharField(
        db_column='marca',
        null=False,
        default='',
        max_length=70
    )
    preco = models.FloatField(
        db_column='preco',
        null=False
    )
    categoria = models.ForeignKey(
        Categoria,
        db_column='id_categoria',
        null=False,
        on_delete=models.DO_NOTHING
    )
    imagem = models.CharField(
        db_column='imagem',
        null=False,
        default='',
        max_length=250
    )

    def __str__(self):
        return (f"{self.id} - {self.categoria.nome_categoria}: "
                f"{self.descricao[:80]}...")


class Fornecedor(ModelBase):
    nome_fornecedor = models.CharField(
        db_column='nome_fornecedor',
        null=False,
        default='',
        max_length=70
    )
    telefone = models.CharField(
        db_column='telefone',
        null=False,
        default='',
        max_length=20
    )

    def __str__(self):
        return f"{self.id} - {self.nome_fornecedor}"

class ProdutoFornecedor(ModelBase):
    produto = models.ForeignKey(
        Produto,
        db_column='id_produto',
        null=False,
        on_delete=models.DO_NOTHING
    )
    fornecedor = models.ForeignKey(
        Fornecedor,
        db_column='id_fornecedor',
        null=False,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return (f"Produto: {self.produto}, "
                f"Fornecedor: {self.fornecedor}")