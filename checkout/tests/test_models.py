# coding=utf-8

from django.test import TestCase

from model_mommy import mommy

from checkout.models import CarrinhoItem


class CartItemTestCase(TestCase):

    def setUp(self):
        mommy.make(CarrinhoItem, _quantity=3)

    def test_post_save_cart_item(self):
        cart_item = CarrinhoItem.objects.all()[0]
        cart_item.quantidade = 0
        cart_item.save()
        self.assertEquals(CarrinhoItem.objects.count(), 2)
