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

    def get(self, request, *args, **kwargs):
        session_key = request.session.session_key
        if session_key and CarrinhoItem.objects.filter(carrinho_key=session_key).exists():
            cart_items = CarrinhoItem.objects.filter(carrinho_key=session_key)
            pedido = Pedido.objects.create_order(
                usuario=request.user, cart_items=cart_items
            )
        else:
            messages.info(request, 'Não há itens no carrinho de compras')
            return redirect('cart_item')
        return super(CheckoutView, self).get(request, *args, **kwargs)

checkout = CheckoutView.as_view()