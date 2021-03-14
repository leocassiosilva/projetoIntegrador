from django.urls import path
from .views import CategoryCreate, ProductCreate, ProductListView, ProductUpdateView

urlpatterns = [
    path('cadastrarCategoria/', CategoryCreate.as_view(), name='cadastrarCategoria'),
    path('cadastrarProduto/', ProductCreate.as_view(), name='cadastrarProduto'),
    path('lista/', ProductListView.as_view(), name='produtos_lista'),
    path('editar/<int:pk>',  ProductUpdateView.as_view(), name='produtos_update'),

]
