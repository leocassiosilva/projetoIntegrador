from django.test import TestCase, Client
from django.urls import reverse
from model_mommy import mommy

from product.models import Product

# Teste de unitario cadastro de produto

class ProdutoViewTestCase(TestCase):

    def test_cadastroProduto(self):
        response = self.client.get(reverse('cadastrar'))
        self.assertEquals(response.status_code, 200)

#Teste de cadastrar produtos
class CadastraViewTesteCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('cadastrarProduto')

    def test_cadastro_error(self):
        data = {'name': 'Feijão',
                'category': 'Legume',
                'quantity': '10',
                'description': 'Feijão Carióca',
                'price': '15'
                }
        response = self.client.post(self.register_url, data)
        self.assertFormError(response, 'form', 'Este campo é obrigatorio.')


    def setUp(self):
        self.client = Client()
        self.register_url1 = reverse('cadastrarProduto')

    def test_cadastro_sucess(self):
        data = {'name': 'Feijão',
                'category': 'Legume',
                'quantity': '10',
                'description': 'Feijão Carióca',
                'price': '15'
                }
        response = self.client.post(self.register_url1, data)
        self.assertEquals(response.status_code, 200)

#Teste de listar produtos
class ProductListTestCase(TestCase):

    def setUp(self):
        self.url = reverse('produtos_lista')
        self.client = Client()
        self.products = mommy.make('product.Product', _quantity=10)

    def tearDown(self):
        Product.objects.all().delete()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register/product_list.html')

    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('product_list' in response.context)
        product_list = response.context['product_list']
        self.assertEquals(product_list.count(), 10)