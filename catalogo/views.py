from rest_framework import viewsets, permissions
from catalogo.models import Produto, Categoria, Fornecedor, ProdutoFornecedor
from catalogo.serializers import ProdutoSerializer, CategoriaSerializer, FornecedorSerializer, ProdutoFornecedorSerializer
from django_filters.rest_framework import DjangoFilterBackend
from catalogo.filters import ProdutoFilter, CategoriaFilter, FornecedorFilter, ProdutoFornecedorFilter, CategoriaFilter


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend,]
    filter_class = ProdutoFilter


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, ]
    filter_class = CategoriaFilter

class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, ]
    filter_class = FornecedorFilter

class ProdutoFornecedorViewSet(viewsets.ModelViewSet):
    queryset = ProdutoFornecedor.objects.all()
    serializer_class = ProdutoFornecedorSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, ]
    filter_class = ProdutoFornecedorFilter
