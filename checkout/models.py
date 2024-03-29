from django.db import models


class CarrinhoManager(models.Manager):

    def add_item(self, carrinho_key, product):
        if self.filter(carrinho_key=carrinho_key, product=product).exists():
            created = False
            carrinhoItem = self.get(carrinho_key=carrinho_key, product=product)
            carrinhoItem.quantidade = carrinhoItem.quantidade + 1
            carrinhoItem.save()
        else:
            created = True
            carrinhoItem = CarrinhoItem.objects.create(
                carrinho_key=carrinho_key, product=product, preco=product.price
            )
        return carrinhoItem, created


class CarrinhoItem(models.Model):
    carrinho_key = models.CharField('Chave do Carrinho', max_length=40, db_index=True)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='Produto')
    quantidade = models.PositiveIntegerField('Quantidade', default=1)
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=8)

    objects = CarrinhoManager()

    class Meta:
        verbose_name = 'Item do carrinho'
        verbose_name_plural = 'Itens do Carrinho'
        unique_together = (('carrinho_key', 'product'),)

    def __str__(self):
        return '{} [{}]'.format(self.product, self.quantidade)


def post_save_cart_item(instance, **kwargs):
    if instance.quantidade < 1:
        instance.delete()


models.signals.post_save.connect(
    post_save_cart_item, sender=CarrinhoItem, dispatch_uid='post_save_cart_item'
)
