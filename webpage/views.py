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
    login_url = reverse_lazy('login')
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        produto = [produto.id for produto in Product.objects.filter(id_usuario=self.request.user)]
        pedido = [pedido for pedido in Pedido.objects.all()]
        pedidos_items = list(PedidoItem.objects.filter(pedido__in=pedido, product__in=produto))

        qtd_pedidos = PedidoItem.objects.filter(pedido__in=pedido).count()
        context['qtd_pedidos'] = qtd_pedidos
        context['pedidos_items'] = pedidos_items
        return context
