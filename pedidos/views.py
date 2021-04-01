from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import RedirectView, TemplateView, ListView, DetailView, UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from rolepermissions.mixins import HasRoleMixin

from checkout.models import CarrinhoItem
from product.models import Product
from .models import Pedido, PedidoItem


# Create your views here.
class CheckoutView(LoginRequiredMixin, HasRoleMixin, TemplateView):
    template_name = 'pedido/pedidos.html'
    allowed_roles = 'cliente'

    def get(self, request, *args, **kwargs):
        session_key = request.session.session_key
        if session_key and CarrinhoItem.objects.filter(carrinho_key=session_key).exists():
            cart_items = CarrinhoItem.objects.filter(carrinho_key=session_key)
            pedido = Pedido.objects.create_order(
                usuario=request.user, cart_items=cart_items)
        else:
            messages.info(request, 'Não há itens no carrinho de compras')
            return redirect('cart_item')

        return super(CheckoutView, self).get(request, *args, **kwargs)


class PedidoListView(LoginRequiredMixin, HasRoleMixin, ListView):
    template_name = 'pedido/pedidos_list.html'
    allowed_roles = 'cliente'
    paginate_by = 7

    def get_queryset(self):
        pedidos = Pedido.objects.filter(usuario=self.request.user)
        return pedidos


class PedidoDetailView(TemplateView):
    template_name = 'pedido/pedidos_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get("pk")
        items_pedidos = PedidoItem.objects.filter(pedido=pk)
        # print(items_pedidos.product)
        # products = Product.objects.filter(product=)

        context['items'] = list(items_pedidos)
        return context


class PedidoDetailsView(DetailView):
    template_name = 'pedido/pedidos_detail.html'

    def get_queryset(self):
        return Pedido.objects.filter(usuario=self.request.user)


class PedidoUpdate(LoginRequiredMixin, HasRoleMixin, UpdateView):
    model = Pedido
    fields = ['status']
    allowed_roles = 'vendedor'
    template_name = 'pedido/pedido_update.html'
    success_url = reverse_lazy('vendedor_vendas')


checkout = CheckoutView.as_view()

pedidoList = PedidoListView.as_view()

pedidoDetail = PedidoDetailView.as_view()

detailPeddio = PedidoDetailsView.as_view()

pedidoUpdate = PedidoUpdate.as_view()