from django.db import models
from django.conf import settings
from checkout.models import CarrinhoItem

class PedidoManager(models.Manager):

    def create_order(self, usuario, cart_items):
        pedido = self.create(usuario=usuario)
        for cart_item in cart_items:
            order_item = PedidoItem.objects.create(
                pedido=pedido, quantidade=cart_item.quantidade, product=cart_item.product,
                preco=cart_item.preco
            )
        return pedido

class PedidoManage(models.Model):

    def create_pedido(self, user, carrinho_items):
        pedido = self.create(User=user)
        for carrinho_item in carrinho_items:
            pedido_item = PedidoItem.objects.create(
                pedido=pedido, quantidade=carrinho_item.quantidade, product=carrinho_item.product,
                preco=carrinho_item.preco
            )
        return pedido


class Pedido(models.Model):
    STATUS_CHOICES = (
        (0, 'Concluido'),
        (1, 'Cancelado'),
        (2, 'Agurdando Pagamento'),
    )

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Usuário')
    status = models.IntegerField('Situação', choices=STATUS_CHOICES, default=0, blank=True)
    data_criacao = models.DateTimeField('Criado em', auto_now_add=True)
    data_modificacao = models.DateTimeField('Modificado em', auto_now=True)

<<<<<<< HEAD
    objects = PedidoManager()
=======
    objects = PedidoManage()

    def __str__(self):
        return 'Pedido #{}'.format(self.pk)
>>>>>>> origin/main

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return 'Pedido #{}'.format(self.pk)


class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, verbose_name='Pedido', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='Produto')
    quantidade = models.PositiveIntegerField('Quantidade', default=1)
    preco = models.DecimalField('Preco', decimal_places=3, max_digits=13)

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens do pedidos'


    def __str__(self):
        return '[{}] {}'.format(self.pedido, self.product)
