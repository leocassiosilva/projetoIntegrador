from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

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
        print(produto)

        pd = PedidoItem.objects.filter(product__in=produto)

        print(pd)
        pedido = [pedido for pedido in Pedido.objects.all()]

        pedidos_items = list(PedidoItem.objects.filter(pedido__in=pedido))
        context['pedidos_items'] = pedidos_items
        print(pedidos_items)
        return context
