from django.shortcuts import render
from datetime import datetime

# Create your views here.
from django.views.generic import ListView, DetailView

from accounts.models import CustomUsuario
from pedidos.models import Pedido, PedidoItem
from product.models import Product
from projetoIntegrador.roles import Vendedor


class VendedoresListView(ListView):
    template_name = 'vendedor/vendedor_list.html'
    model = CustomUsuario
    paginate_by = 6

    def get_queryset(self):
        vendedor = CustomUsuario.objects.filter(groups__name='vendedor')
        return vendedor


class MinhasVendasListView(ListView):
    template_name = 'vendedor/vendas_list.html'
    model = Pedido

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        produto = [produto.id for produto in Product.objects.filter(id_usuario=self.request.user)]
        pedido = [pedido for pedido in Pedido.objects.all()]
        pedidos_items = list(PedidoItem.objects.filter(pedido__in=pedido, product__in=produto))
        context['pedidos_items'] = pedidos_items
        return context


class MinhasVendasDetails(DetailView):
    template_name = 'vendedor/vendas_detalhe.html'
    model = Pedido

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)
        produto = [produto.id for produto in Product.objects.filter(id_usuario=self.request.user)]
        pedidos_items = PedidoItem.objects.filter(pedido=pk, product__in=produto)
        print(pedidos_items)
        data_atual = datetime.now()
        context['data_atual'] = data_atual
        context['pedidos_items'] = pedidos_items
        return context
