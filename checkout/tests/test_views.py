# coding=utf-8

from django.test import Client, TestCase
from django.urls import reverse

from model_mommy import mommy

from checkout.models import CarrinhoItem


class CreateCartItemTestCase(TestCase):

    def setUp(self):
        self.product = mommy.make('Product')
        self.client = Client()
        self.url = reverse(
            'create_cartitem', kwargs={'slug': self.product.slug}
        )

    def tearDown(self):
        self.product.delete()
        CarrinhoItem.objects.all().delete()

    def test_add_cart_item_simple(self):
        response = self.client.get(self.url)
        redirect_url = reverse('cart_item')
        self.assertRedirects(response, redirect_url)
        self.assertEquals(CarrinhoItem.objects.count(), 1)

    def test_add_cart_item_complex(self):
        response = self.client.get(self.url)
        response = self.client.get(self.url)
        cart_item = CarrinhoItem.objects.get()
        self.assertEquals(cart_item.quantity, 2)
