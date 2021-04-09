from datetime import datetime

from django.db.models import Sum, Count, Min
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from accounts.models import CustomUsuario
from pedidos.models import PedidoItem, Pedido
from product.models import Product


def home(request):
    return render(request, 'home.html')


class IndexView(LoginRequiredMixin, TemplateView):
    model = Pedido
    readonly_fields = ("data_criacao")
    login_url = reverse_lazy('login')
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = datetime.now()
        produto = [produto.id for produto in Product.objects.filter(id_usuario=self.request.user)]
        pd = Product.objects.filter(pk=1)

        pedido = [pedido for pedido in Pedido.objects.filter(data_criacao__month=now.month)]

        # Quantidade de pedidos do mês
        pedidos_items = list(PedidoItem.objects.filter(pedido__in=pedido, product__in=produto))
        context['pedidos_items'] = pedidos_items
        # valor vendido do mês
        valor_vendido = PedidoItem.objects.filter(pedido__in=pedido, product__in=produto).aggregate(Sum('preco'))
        context['valor_vendido'] = valor_vendido
        # valor quantidade de produtos do mes
        qtd_produtos = PedidoItem.objects.filter(pedido__in=pedido, product__in=produto).aggregate(Sum('quantidade'))
        qtd_pedidos = PedidoItem.objects.filter(pedido__in=pedido).count()
        # pedidos do mes
        pedidos_mes = Pedido.objects.filter(data_criacao__month=now.month).count()
        todos_pedidos = [pedido for pedido in Pedido.objects.all()]
        total_vendido = PedidoItem.objects.filter(pedido__in=todos_pedidos, product__in=produto).aggregate(Sum('preco'))
        context['total_vendido'] = total_vendido

        total_produtos = PedidoItem.objects.filter(pedido__in=todos_pedidos, product__in=produto).aggregate(
            Sum('quantidade'))



        pr = Product.objects.all().annotate(country_quantity=Sum('quantity')).filter(status=0,
                                                          country_quantity__gt=10)[:8]
        print(pr)
        context['produtos'] = pr
        context['total_produtos'] = total_produtos
        context['pedidos_mes'] = pedidos_mes
        context['qtd_produtos'] = qtd_produtos
        context['qtd_pedidos'] = qtd_pedidos
        context['pedidos_items'] = pedidos_items
        # Fim pedidos do mês

        return context

    def product_chart(request):
        produto = Product.objects.filter(id_usuario=request.user.id)

        produtos = PedidoItem.objects.filter(product__in=produto).values('product__name').annotate(Sum('quantidade'))[
                   :5]

        print(produtos)
        labels = []
        data = []

        for cont in produtos:
            labels.append(cont['product__name'])
            data.append(cont['quantidade__sum'])

        return JsonResponse(data={
            'labelsR': labels,
            'dataR': data,
        })
