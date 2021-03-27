from django.db import models


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

    id = models.AutoField(primary_key=True, db_column="id_pedido")
    usuario = models.ForeignKey("accounts.CustomUsuario", on_delete=models.CASCADE, db_column="id_usuario")
    status = models.IntegerField('Situação', choices=STATUS_CHOICES, default=0, blank=True)
    data_criacao = models.DateTimeField('Criado em', auto_now_add=True)
    data_modificacao = models.DateTimeField('Modificado em', auto_now=True)

    objects = PedidoManage()

    def __str__(self):
        return 'Pedido #{}'.format(self.pk)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        db_table = "Pedidos"
        managed = True


class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, verbose_name='Pedido', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='Produto')
    quantidade = models.PositiveIntegerField('Quantidade', default=1)
    preco = models.DecimalField('Preco', decimal_places=3, max_digits=13)

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens do pedidos'
        db_table = "Itens_pedido"
        managed = True

    def __str__(self):
        return '[{}] {}'.format(self.pedido, self.product)
