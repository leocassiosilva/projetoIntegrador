from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import RedirectView, TemplateView
from django.contrib import messages
from product.models import Product
from .models import CarrinhoItem
from django.forms import modelformset_factory
from django.db.models import Sum
from django import forms


class CreateCarrinhoItemView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        product = get_object_or_404(Product, slug=self.kwargs['slug'])
        if self.request.session.session_key is None:
            self.request.session.save()
        carrinhoItem, created = CarrinhoItem.objects.add_item(
            self.request.session.session_key, product
        )
        if created:
            messages.success(self.request, 'Produto adicionado com sucesso')
        else:
            messages.success(self.request, 'Produto atualizado com sucesso')
        return reverse('cart_item')

create_cartitem = CreateCarrinhoItemView.as_view()


class CartItemView(TemplateView):
    template_name = 'checkout/cart.html'

    def get_formset(self, clear=False):
        CartItemFormSet = modelformset_factory(
            CarrinhoItem, fields=('quantidade',), can_delete=True, extra=0
        )
        session_key = self.request.session.session_key
        if session_key:
            if clear:
                formset = CartItemFormSet(
                    queryset=CarrinhoItem.objects.filter(carrinho_key=session_key)
                )
            else:
                formset = CartItemFormSet(
                    queryset=CarrinhoItem.objects.filter(carrinho_key=session_key),
                    data=self.request.POST or None
                )
        else:
            formset = CartItemFormSet(queryset=CarrinhoItem.objects.none())
        return formset

    def get_context_data(self, **kwargs):
        context = super(CartItemView, self).get_context_data(**kwargs)
        context['formset'] = self.get_formset()
        return context

    def post(self, request, *args, **kwargs):
        formset = self.get_formset()
        context = self.get_context_data(**kwargs)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Carrinho atualizado com sucesso')
            context['formset'] = self.get_formset(clear=True)
        return self.render_to_response(context)

cart_item = CartItemView.as_view()
