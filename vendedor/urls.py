from django.urls import path, re_path
from .views import VendedoresListView, MinhasVendasListView, MinhasVendasDetails

urlpatterns = [
    path('bancas/', VendedoresListView.as_view(), name='vendedor_banca'),
    path('vendas/', MinhasVendasListView.as_view(), name='vendedor_vendas'),
    path('detalhe/<int:pk>/', MinhasVendasDetails.as_view(), name='vendas_detalhe'),
]
