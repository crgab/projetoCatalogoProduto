from rest_framework import serializers
from catalogo.models import Categoria, Produto, Fornecedor, ProdutoFornecedor

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'descricao', 'marca', 'preco', 'categoria']


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'


class ProdutoFornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoFornecedor
        fields = '__all__'
