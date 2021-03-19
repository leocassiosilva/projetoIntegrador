from django.db import models


class CarrinhoManager(models.Manager):

    def add_item(selfself, carrinho_key, produto):
        pass


class CarrinhoItem(models.Model):
    carrinho_key = models.CharField('Chave do Carrinho', max_length=40, db_index=True)
    produto = models.ForeignKey('product.Product', models.DO_NOTHING, db_column='id_produto', blank=True, null=True)
    quantidade = models.PositiveIntegerField('Quantidade', default=1)
    preco = models.DecimalField('Preco', decimal_places=10,  max_digits=12)

    object = CarrinhoManager()

    class Meta:
        verbose_name = 'Item do carrinho'
        verbose_name_plural = 'Itens do Carrinho'
        unique_together = (('carrinho_key', 'produto'),)

    def __str__(self):
        return '{} [{}]'.format(self.produto, self.quantidade)
