from django.test import TestCase

from model_mommy import mommy

from checkout.models import CarrinhoItem

class CarrinhoItemTestCase(TestCase):

    def setUp(self):
        mommy.make(CarrinhoItem, _quantity=3)


    def test_post_save_carrinho_item(self):
        carrinhoItem = CarrinhoItem.objects.all()[0]
        carrinhoItem.quantidade = 0
        carrinhoItem.save()
        self.assertEquals(CarrinhoItem.objects.count(), 3)

