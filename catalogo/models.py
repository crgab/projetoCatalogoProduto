from django.db import models

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
        max_length=70
    )

    def __str__(self):
        return f"{self.id} - {self.nome_categoria}:"


class Produto(ModelBase):
    descricao = models.CharField(
        db_column='descricao',
        null=False,
        max_length=70
    )
    marca = models.CharField(
        db_column='marca',
        null=False,
        max_length=70
    )
    preco = models.FloatField(
        db_column='preco',
        null=False
    )
    id_categoria = models.ForeignKey(
        Categoria,
        db_column='id_categoria',
        null=False,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return (f"{self.id} - {self.descricao}, "
                f"Marca: {self.marca}:")


class Fornecedor(ModelBase):
    nome_fornecedor = models.CharField(
        db_column='nome_fornecedor',
        null=False,
        max_length=70
    )
    telefone = models.CharField(
        db_column='telefone',
        null=False,
        max_length=20
    )

    def __str__(self):
        return f"{self.id} - {self.nome_fornecedor}"

class ProdutoFornecedor(ModelBase):
    id_produto = models.ForeignKey(
        Produto,
        db_column='id_produto',
        null=False,
        on_delete=models.DO_NOTHING
    )
    id_fornecedor = models.ForeignKey(
        Fornecedor,
        db_column='id_fornecedor',
        null=False,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return (f"Produto: {self.id_produto}, "
                f"Fornecedor: {self.id_fornecedor}")