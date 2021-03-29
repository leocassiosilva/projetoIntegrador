from django.test import Client, TestCase
from django.conf import settings
from django.urls import reverse

from model_mommy import mommy

from checkout.models import CarrinhoItem


class PedidoViewTestCase(TestCase):

    def setUp(self):
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('123')
        self.user.save()
        self.cart_item = mommy.make(CarrinhoItem)
        self.client = Client()
        self.checkout_url = reverse('pedidos')

    def test_pedido_view(self):
        response =self.client.get(self.checkout_url)
        redirect_url = '{}?next={}'.format(
            reverse(settings.LOGIN_URL), self.checkout_url
        )
        self.assertRedirects(response, redirect_url)
