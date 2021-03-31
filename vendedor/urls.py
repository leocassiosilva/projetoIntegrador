from django.urls import path, re_path
from .views import VendedoresListView, MinhasVendasListView

urlpatterns = [
    path('bancas/', VendedoresListView.as_view(), name='vendedor_banca'),
    path('vendas/', MinhasVendasListView.as_view(), name='vendedor_vendas'),
]
