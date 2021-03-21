from django.shortcuts import get_object_or_404

# Create your views here.

from django.views.generic import RedirectView
from .models import CarrinhoItem
from product.models import Product
from django.contrib import messages


class CreateCarrinhoItemView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        product = get_object_or_404(Product, slug=self.kwargs['slug'])
        carrinho = CarrinhoItem.objects.add_item(
            self.request.session.session_key, product
        )
        messages.success(self.request, 'Produto Adicionado com Sucesso!')
        return product.get_absolute_url()

