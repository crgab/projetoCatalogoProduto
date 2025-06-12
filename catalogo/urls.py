from django.urls import path, include
from rest_framework.routers import DefaultRouter
from catalogo.views import ProdutoViewSet, CategoriaViewSet, FornecedorViewSet, ProdutoFornecedorViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'fornecedors', FornecedorViewSet)
router.register(r'produtofornecedors', ProdutoFornecedorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]