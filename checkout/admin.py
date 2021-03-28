from django.contrib import admin

from .models import CarrinhoItem
from pedidos.models import Pedido, PedidoItem

admin.site.register([CarrinhoItem, Pedido, PedidoItem])