import django_filters
from catalogo.models import Produto, Fornecedor, ProdutoFornecedor, Categoria

class ProdutoFilter(django_filters.FilterSet):
    descricao = django_filters.CharFilter(lookup_expr='icontains')
    categoria = django_filters.CharFilter(lookup_expr='icontains')
    marca = django_filters.CharFilter(lookup_expr='icontains')
    preco = django_filters.CharFilter(lookup_expr='exact')


    class Meta:
        model = Produto
        fields = ['descricao', 'categoria', 'marca', 'preco']


class CategoriaFilter(django_filters.FilterSet):
    nome_categoria = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Categoria
        fields = ['id', 'nome_categoria']


class FornecedorFilter(django_filters.FilterSet):
    nome_fornecedor = django_filters.CharFilter(lookup_expr='icontains')
    telefone = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Fornecedor
        fields = ['id', 'nome_fornecedor', 'telefone']


class ProdutoFornecedorFilter(django_filters.FilterSet):
    produto_id = django_filters.NumberFilter(field_name='produto_id')
    nome_produto = django_filters.CharFilter(field_name='nome_produto', lookup_expr='icontains')
    fornecedor_id = django_filters.NumberFilter(field_name='fornecedor_id')
    nome_fornecedor = django_filters.CharFilter(field_name='nome_fornecedor', lookup_expr='icontains')

    class Meta:
        model = ProdutoFornecedor
        fields = ['id', 'produto_id', 'fornecedor_id']