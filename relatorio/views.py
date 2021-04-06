from PyPDF2.pdf import BytesIO
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.
from django.template.loader import get_template
from django.views.generic.base import View, TemplateView
from reportlab.pdfgen import canvas
from rolepermissions.mixins import HasRoleMixin

from pedidos.models import PedidoItem, Pedido
from product.models import Product
from projetoIntegrador.utils import render_to_pdf  # created in step 4


class TemplateRelatorio(LoginRequiredMixin, HasRoleMixin, TemplateView):
    template_name = 'produtos/baixar_relatorio.html'
    allowed_roles = 'vendedor'


class GeneratePdf(View):

    def get(self, request, *args, **kwargs):
        now = datetime.now()
        produto = Product.objects.filter(id_usuario=request.user.id)
        pedidos_mes = Pedido.objects.filter(data_criacao__month=now.month)
        produtos = PedidoItem.objects.filter(product__in=produto, pedido__in=pedidos_mes).values('product__name',
                                                                                                 'product__price',
                                                                                                 'pedido__id').annotate(
            Sum('quantidade'))
        data_atual = datetime.now()
        data = {'produtos': produtos, 'data': data_atual}

        pdf = render_to_pdf('produtos/relatorio.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('produtos/relatorio.html')

        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('produtos/relatorio.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


def write_pdf_view(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'

    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    # Start writing the PDF here
    p.drawString(100, 100, 'Hello world.')
    # End writing

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response