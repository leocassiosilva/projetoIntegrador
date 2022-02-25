from django.db.models import Sum
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import RedirectView, TemplateView, ListView, DetailView, UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from rolepermissions.mixins import HasRoleMixin
from checkout.models import CarrinhoItem
from product.models import Product
from .models import Pedido, PedidoItem


def test():
    return "ola"


class CheckoutView(LoginRequiredMixin, TemplateView):
    template_name = 'pedido/pedidos.html'

    def get(self, request, *args, **kwargs):
        session_key = request.session.session_key
        print(session_key)
        if session_key and CarrinhoItem.objects.filter(carrinho_key=session_key).exists():
            cart_item = CarrinhoItem.objects.filter(carrinho_key=session_key)

            pedido = Pedido.objects.create_order(
                usuario=request.user, cart_items=cart_item)

            for est in cart_item:
                # print(est.product.id)
                sub_qtd = Product.objects.filter(id=est.product.id)
                for qtd in sub_qtd:
                    total = qtd.quantity - est.quantidade
                    print(total)
                    Product.objects.filter(id=est.product.id).update(quantity=total)
            cart_item.delete()
        else:
            messages.info(request, 'Não há itens no carrinho de compras')
            return redirect('cart_item')
        return super(CheckoutView, self).get(request, *args, **kwargs)


class PedidoListView(LoginRequiredMixin, HasRoleMixin, generic.ListView):
    template_name = 'pedido/pedidos_lists.html'
    allowed_roles = 'cliente'
    model = Pedido
    paginate_by = 6

    def get_queryset(self):
        return Pedido.objects.filter(usuario=self.request.user)


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
