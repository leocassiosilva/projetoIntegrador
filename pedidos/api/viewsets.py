from rest_framework import viewsets

from pedidos.api.serializers import PedidoSerializer, PedidoItemSerializer
from pedidos.models import Pedido


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class PedidoItemViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoItemSerializer
