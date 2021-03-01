from django.urls import path
from .views import CategoryCreate, ProductCreate

urlpatterns = [
    path('cadastrarCategoria/', CategoryCreate.as_view(), name='cadastrarCategoria'),
    path('cadastrarProduto/', ProductCreate.as_view(), name='cadastrarProduto'),
]