from django.test import TestCase
from django.urls import reverse


# Teste de unitario cadastro de produto

# teste para view de cadastro de produto
class ProdutoViewTestCase(TestCase):

    def test_cadastroProduto(self):
        response = self.client.get(reverse('cadastrar'))
        self.assertEquals(response.status_code, 200)


