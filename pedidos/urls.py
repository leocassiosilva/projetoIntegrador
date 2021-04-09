from django.urls import path, include
from rest_framework import routers

from . import views
from .api.viewsets import PedidoViewSet, PedidoItemViewSet

router = routers.DefaultRouter()
router.register(r'pedido', PedidoViewSet)
router.register(r'itemPedido', PedidoItemViewSet)


urlpatterns = [
    path('finalizando/', views.checkout, name='pedidos'),
    path('meusPedidos/', views.pedidoList, name='meus_Pedidos'),
    path('detalhe/<int:pk>/', views.detailPeddio, name='pedidos_detalhe'),
    path('atualizar/<int:pk>/', views.pedidoUpdate, name='pedidos_update'),
    path('', include(router.urls)),

]
