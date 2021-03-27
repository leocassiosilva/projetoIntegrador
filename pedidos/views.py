from django.contrib import messages
from django.shortcuts import render, redirect

from django.views.generic import TemplateView

from checkout.models import CarrinhoItem
from pedidos.models import Pedido


class PedidoView(TemplateView):
    template_name = 'pedidos/pedido.html'

    def get(self, request, *args, **kwargs):
        session_key = request.session.session_key
        if session_key and CarrinhoItem.objects.filter(carrinho_key=session_key).exists():
            carrinho_items = CarrinhoItem.objects.filter(carrinho_key=session_key)
            pedido = Pedido.objects.create_pedido(
                user=request.user, carrinho_items=carrinho_items
            )
        else:
            messages.info(request, 'Não há itens no carrinho de compras')
            return redirect('cart_item')
        return super(PedidoView, self).get(request, *args, **kwargs)
