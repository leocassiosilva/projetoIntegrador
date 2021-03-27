from django.test import TestCase, Client
from django.urls import reverse

class CadastraViewTesteCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('cadastrar')

    '''

    def test_cadastro_ok(self):
        data = {'username': 'francisco@gmail.com',
                'first_name': 'Francisco',
                'last_name': 'Leocassio',
                'telefone': '(84)00000-0000',
                'cep': '654454',
                'cidade': 'Natal',
                'rua': 'Das Almas',
                'bairro': 'Centro',
                'logadouro': 'Casa',
                'numero': 'S/N',
                'password': 'mnbvcxz987654321'}
        response = self.client.post(self.register_url, data)
        self.assertRedirects(response, 'login/')
        self.assertEquals(CustomUsuario.objects.count(), 1)

'''

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

