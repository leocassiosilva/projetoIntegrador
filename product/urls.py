from django.urls import path, include
from rest_framework import routers

from .api.viewsets import ProductViewSet
from .views import CategoryCreate, MedidaCreate, ProductCreate, ProductListView, ProductUpdateView, \
    ProductListViewProdutos, \
    ProductDeleteView, ProdutoSeach, ProductVendedorListViewProdutos


router = routers.DefaultRouter()
router.register(r'produto', ProductViewSet)


urlpatterns = [
    path('cadastrarCategoria/', CategoryCreate.as_view(), name='cadastrarCategoria'),
    path('cadastrarMedida/', MedidaCreate.as_view(), name='cadastrarMedida'),
    path('cadastrarProduto/', ProductCreate.as_view(), name='cadastrarProduto'),
    path('lista/', ProductListView.as_view(), name='produtos_lista'),
    path('editar/<int:pk>', ProductUpdateView.as_view(), name='produto_update'),
    path('deletar/<int:pk>/', ProductDeleteView.as_view(), name='produto_delete'),
    path('lista-produtos/', ProdutoSeach.as_view(), name='lista_produtos'),
    path('todos/', ProductListViewProdutos.as_view(), name='produtos_disponiveis'),
    path('vendedor/<int:pk>', ProductVendedorListViewProdutos.as_view(), name='produtos_vendedor'),
    path('', include(router.urls)),

]
