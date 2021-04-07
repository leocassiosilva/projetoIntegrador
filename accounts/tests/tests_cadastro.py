from django.test import TestCase, Client
from django.urls import reverse

from accounts.models import CustomUsuario


class CadastraViewTesteCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('cadastrar')

    def test_register_ok(self):
        data = {'username': 'leocassio@gmail.com',
                'first_name': 'Francisco',
                'last_name': 'Leocassio',
                'telefone': '(84)00000-0000',
                'cep': '654454',
                'cidade': 'Natal',
                'rua': 'Das Almas',
                'nome_banca': 'Banca Boa',
                'bairro': 'Centro',
                'logadouro': 'Casa',
                'numero': 'S/N',
                'password': 'mnbvcxz987654321'}

        response = self.client.post(self.register_url, data)
        print(response)
        index_url = reverse('login')
        self.assertRedirects(response, index_url)
        self.assertEquals(CustomUsuario.objects.count(), 1)


    def test_cadastro_error(self):
        data = {'username': '',
                'first_name': 'Francisco',
                'last_name': 'Leocassio',
                'telefone': '(84)00000-0000',
                'cep': '654454',
                'cidade': 'Natal',
                'rua': 'Das Almas',
                'nome_banca': 'Banca Boa',
                'bairro': 'Centro',
                'logadouro': 'Casa',
                'numero': 'S/N',
                'password': 'mnbvcxz987654321'}
        response = self.client.post(self.register_url, data)
        self.assertFormError(response, 'form', 'username', 'Este campo é obrigatório.')
