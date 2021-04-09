from django.test import TestCase
from django.urls import reverse
from model_mommy import mommy
from product.models import Category, Product


class ProductTestCase(TestCase):

    def setUp(self):
        self.product = mommy.make(Product, slug='produto')

    def test_get_absolute_url(self):
        self.assertEquals(
            self.product.get_absolute_url(),
            reverse('product', kwargs={'slug': self.category.slug})
        )
