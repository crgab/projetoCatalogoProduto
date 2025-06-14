from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny

from catalogo.models import Produto, Categoria, Fornecedor, ProdutoFornecedor
from catalogo.serializers import ProdutoSerializer, CategoriaSerializer, FornecedorSerializer, ProdutoFornecedorSerializer
from django_filters.rest_framework import DjangoFilterBackend
from catalogo.filters import ProdutoFilter, FornecedorFilter, ProdutoFornecedorFilter, CategoriaFilter


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['descricao', 'categoria', 'marca', 'preco']
    filter_class = ProdutoFilter


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['nome_categoria']
    filter_class = CategoriaFilter

class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['nome_fornecedor', 'telefone']
    filter_class = FornecedorFilter

class ProdutoFornecedorViewSet(viewsets.ModelViewSet):
    queryset = ProdutoFornecedor.objects.all()
    serializer_class = ProdutoFornecedorSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['produto', 'fornecedor']
    filter_class = ProdutoFornecedorFilter
