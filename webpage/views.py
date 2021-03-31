from datetime import datetime

from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from accounts.models import CustomUsuario
from pedidos.models import PedidoItem, Pedido
from product.models import Product


def home(request):
    return render(request, 'home.html')


class IndexView(LoginRequiredMixin, TemplateView):
    model = Pedido
    readonly_fields = ("data_criacao")
    login_url = reverse_lazy('login')
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = datetime.now()
        produto = [produto.id for produto in Product.objects.filter(id_usuario=self.request.user)]

        pedido = [pedido for pedido in Pedido.objects.filter(data_criacao__month=now.month)]

        #Quantidade de pedidos do mês
        pedidos_items = list(PedidoItem.objects.filter(pedido__in=pedido, product__in=produto))
        context['pedidos_items'] = pedidos_items
        #valor vendido do mês
        valor_vendido = PedidoItem.objects.filter(pedido__in=pedido, product__in=produto).aggregate(Sum('preco'))
        context['valor_vendido'] = valor_vendido
        # valor quantidade de produtos do mes
        qtd_produtos = PedidoItem.objects.filter(pedido__in=pedido, product__in=produto).aggregate(Sum('quantidade'))
        qtd_pedidos = PedidoItem.objects.filter(pedido__in=pedido).count()

        pedidos_mes = Pedido.objects.filter(data_criacao__month=now.month).count()
        context['pedidos_mes'] = pedidos_mes
        context['qtd_produtos'] = qtd_produtos
        context['qtd_pedidos'] = qtd_pedidos
        context['pedidos_items'] = pedidos_items
        return context
