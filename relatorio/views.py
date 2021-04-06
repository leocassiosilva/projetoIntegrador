from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from product.models import Product
from projetoIntegrador.utils import render_to_pdf  # created in step 4


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        produtos = Product.objects.order_by('name').filter(id_usuario=self.request.user)
        data = {'produtos': produtos}

        pdf = render_to_pdf('produtos/relatorio.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

