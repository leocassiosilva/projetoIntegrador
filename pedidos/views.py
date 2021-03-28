from django.shortcuts import get_object_or_404, redirect
from django.views.generic import RedirectView, TemplateView, ListView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from rolepermissions.mixins import HasRoleMixin

from checkout.models import CarrinhoItem
from .models import Pedido


# Create your views here.
class CheckoutView(LoginRequiredMixin, HasRoleMixin, TemplateView):
    template_name = 'pedido/pedidos.html'

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

    def get_queryset(self):
        pedidos = Pedido.objects.filter(usuario=self.request.user)
        return pedidos


checkout = CheckoutView.as_view()

pedidoList = PedidoListView.as_view()
