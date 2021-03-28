<<<<<<< HEAD
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import RedirectView, TemplateView
from django.forms import modelformset_factory
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from product.models import Product

from checkout.models import CarrinhoItem
from .models import Pedido

# Create your views here.
class CheckoutView(LoginRequiredMixin, TemplateView):

    template_name = 'pedido/pedidos.html'
=======
from django.contrib import messages
from django.shortcuts import render, redirect

from django.views.generic import TemplateView

from checkout.models import CarrinhoItem
from pedidos.models import Pedido


class PedidoView(TemplateView):
    template_name = 'pedidos/pedido.html'
>>>>>>> origin/main

    def get(self, request, *args, **kwargs):
        session_key = request.session.session_key
        if session_key and CarrinhoItem.objects.filter(carrinho_key=session_key).exists():
<<<<<<< HEAD
            cart_items = CarrinhoItem.objects.filter(carrinho_key=session_key)
            pedido = Pedido.objects.create_order(
                usuario=request.user, cart_items=cart_items
=======
            carrinho_items = CarrinhoItem.objects.filter(carrinho_key=session_key)
            pedido = Pedido.objects.create_pedido(
                user=request.user, carrinho_items=carrinho_items
>>>>>>> origin/main
            )
        else:
            messages.info(request, 'Não há itens no carrinho de compras')
            return redirect('cart_item')
<<<<<<< HEAD
        return super(CheckoutView, self).get(request, *args, **kwargs)

checkout = CheckoutView.as_view()
=======
        return super(PedidoView, self).get(request, *args, **kwargs)
>>>>>>> origin/main
