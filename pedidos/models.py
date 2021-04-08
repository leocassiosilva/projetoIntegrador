from django.db import models
from django.conf import settings
from product.models import Product

class PedidoManager(models.Manager):
    def create_order(self, usuario, cart_items):
        pedido = self.create(usuario=usuario)
        for cart_item in cart_items:
            order_item = PedidoItem.objects.create(
                pedido=pedido, quantidade=cart_item.quantidade, product=cart_item.product,
                preco=cart_item.preco
            )
        return pedido

class Pedido(models.Model):
    STATUS_CHOICES = (
        (0, 'Pedido Efetuado'),
        (1, 'Pedido Enviado'),
        (2, 'Pedido Cancelado'),
        (3, 'Pedido Finalizado')
    )

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Usuário')
    status = models.IntegerField('Situação', choices=STATUS_CHOICES, default=0, blank=True)
    data_criacao = models.DateTimeField('Criado em', auto_now_add=True)
    data_modificacao = models.DateTimeField('Modificado em', auto_now=True)

    objects = PedidoManager()

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def _str_(self):
        return 'Pedido #{}'.format(self.pk)

    def products(self):
        products_ids = self.items.values_list('product')
        return Product.objects.filter(pk__in=products_ids)

    def total(self):
        tota_produtos = self.items.aggregate(
            total=models.Sum(
                models.F('preco') * models.F('quantidade'),
                output_field=models.DecimalField()
            )
        )
        return tota_produtos['total']

class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, verbose_name='Pedido', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='Produto',related_name='produtos')
    quantidade = models.PositiveIntegerField('Quantidade', default=1)
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=8)

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens do pedidos'

    def _str_(self):
        return '[{}] {}'.format(self.pedido, self.product)
