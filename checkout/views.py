from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView
from django.contrib import messages
from product.models import Product
from .models import CarrinhoItem


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
        return product.get_absolute_url()

create_cartitem = CreateCarrinhoItemView.as_view()

