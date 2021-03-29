from django.conf import settings
from django.test import TestCase

# Create your tests here.
from model_mommy import mommy

from checkout.models import CarrinhoItem
from pedidos.models import Pedido


class PedidoTestCase(TestCase):

    def setUp(self):
        self.cart_item = mommy.make(CarrinhoItem)
        self.user = mommy.make(settings.AUTH_USER_MODEL)

    def test_create_pedido(self):
        Pedido.objects.create_order(self.user, [self.cart_item])
        self.assertEquals(Pedido.objects.count(), 1)

        pedido = Pedido.objects.get()
        self.assertEquals(pedido.usuario, self.user)

        pedido_item = pedido.items.get()
        self.assertEquals(pedido_item.product, self.cart_item.product)
