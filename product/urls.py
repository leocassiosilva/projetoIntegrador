from django.urls import path
from .views import CategoryCreate, ProductCreate, ProductListView, ProductUpdateView, ProductListViewProdutos, \
    ProductDeleteView, ProdutoSeach, autoCompleteProdutos

urlpatterns = [
    path('cadastrarCategoria/', CategoryCreate.as_view(), name='cadastrarCategoria'),
    path('cadastrarProduto/', ProductCreate.as_view(), name='cadastrarProduto'),
    path('lista/', ProductListView.as_view(), name='produtos_lista'),
    path('editar/<int:pk>', ProductUpdateView.as_view(), name='produto_update'),
    path('deletar/<int:pk>/', ProductDeleteView.as_view(), name='produto_delete'),
    path('lista-produtos/', ProdutoSeach.as_view(), name='lista_produtos'),
    path('todos/', ProductListViewProdutos.as_view(), name='produtos_disponiveis'),


]
