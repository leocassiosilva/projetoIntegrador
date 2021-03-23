from django.test import TestCase, Client
from django.urls import reverse

from accounts.models import CustomUsuario


class CadastraViewTesteCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('accounts:cadastrar')

    def test_cadastro_error(self):
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
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatorio.')

        # self.assertEquals(response.status_code, 200)

    def setUp(self):
        self.client = Client()
        self.register_url1 = reverse('cadastrar')

    # Esse teste não funciona, tentei mais ele não vai
    def test_cadastro_sucess(self):
        data = {'email': 'francisco@gmail.com',
                'username': 'francisco@gmail.com',
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
        index_url = reverse('login')
        self.assertRedirects(response, index_url)
        self.assertEquals(CustomUsuario.objects.count(), 1)
