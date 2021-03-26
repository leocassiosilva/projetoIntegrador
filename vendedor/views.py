from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from accounts.models import CustomUsuario
from product.models import Product
from projetoIntegrador.roles import Vendedor


class VendedoresListView(ListView):
    template_name = 'vendedor/vendedor_list.html'
    model = CustomUsuario
    paginate_by = 6

    def get_queryset(self):
        vendedor = CustomUsuario.objects.filter(groups__name='vendedor')
        return vendedor



