from django.shortcuts import render
from rest_framework import viewsets

from catalogo.models import Produto, Categoria, Fornecedor, ProdutoFornecedor
from catalogo.serializers import ProdutoSerializer, CategoriaSerializer, FornecedorSerializer, ProdutoFornecedorSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

class ProdutoFornecedorViewSet(viewsets.ModelViewSet):
    queryset = ProdutoFornecedor.objects.all()
    serializer_class = ProdutoFornecedorSerializer

