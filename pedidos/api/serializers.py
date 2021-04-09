from rest_framework import serializers

from pedidos.models import Pedido, PedidoItem


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'


class PedidoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoItem
        fields = '__all__'
