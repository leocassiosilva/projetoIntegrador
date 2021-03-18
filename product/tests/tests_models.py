from django.test import TestCase
from model_mommy import mommy
from product.models import Product


class ProductTestCase(TestCase):

    def setUp(self):
        self.product = mommy.make(Product)

    def test_get_absolute_url(self):
        self.assertTrue(Product(self.product, Product))
        self.assertEquals(self.product.__str__(), self.product.name)

