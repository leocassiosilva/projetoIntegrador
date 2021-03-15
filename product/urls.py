from django.urls import path
from .views import CategoryCreate, ProductCreate, ProductListView, ProductUpdateView, ProductListViewProdutos

urlpatterns = [
    path('cadastrarCategoria/', CategoryCreate.as_view(), name='cadastrarCategoria'),
    path('cadastrarProduto/', ProductCreate.as_view(), name='cadastrarProduto'),
    path('lista/', ProductListView.as_view(), name='produtos_lista'),
    path('editar/<int:pk>',  ProductUpdateView.as_view(), name='produto_update'),
    path('lista-produtos/', ProductListViewProdutos.as_view(), name='lista_produtos'),

]
