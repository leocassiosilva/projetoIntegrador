from django.test import TestCase, Client
from django.urls import reverse

from model_mommy import mommy

from checkout.models import CarrinhoItem


class CreateCarrinhoItemTestCase(TestCase):

    def setUp(self):
        self.product = mommy.make('product.Product')
        self.client = Client()
        self.url = reverse('criar_carrinhoitem', kwargs={'slug': self.product.slug})

    def tearDown(self):
        self.product.delete()
        CarrinhoItem.objects.all().delete()

    def test_add_carrinho_item(self):
        response = self.client.get(self.url)
        redirect_url = reverse('cart_item')
        self.assertRedirects(response, redirect_url)
        self.assertEquals(CarrinhoItem.objects.count(), 1)

    def test_add_carrinho_item_dois_products(self):
        response = self.client.get(self.url)
        response = self.client.get(self.url)
        carrinho_item = CarrinhoItem.objects.get()
        self.assertEquals(carrinho_item.quantidade, 2)
