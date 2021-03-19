from django.test import TestCase, Client
from django.urls import reverse


# teste para view de cadastro de usuario
class UsuarioViewTestCase(TestCase):

    def test_cadastroUsuario(self):
        response = self.client.get(reverse('cadastrar'))
        self.assertEquals(response.status_code, 200)

    # Esse teste foi proposital para que pudesse dar erro
    def test_password_reset(self):
        response = self.client.get(reverse('password-resetr'))
        self.assertEquals(response.status_code, 200)

    # Esse precisa fazer o login
    def test_update(self):
        response = self.client.get(reverse('atualizar'))
        self.assertEquals(response.status_code, 200)

    # Esse teste server para testar o password reset
    def test_reset_password(self):
        response = self.client.get(reverse('password-reset/'))
        self.assertEquals(response.status_code, 200)

    # Esse teste server para testar o password reset
    def test_reset_password(self):
        response = self.client.get(reverse('password_reset_done'))
        self.assertEquals(response.status_code, 200)

    # Esse teste server para testar o password reset
    def test_password_reset_complete(self):
        response = self.client.get(reverse('password_reset_complete'))
        self.assertEquals(response.status_code, 200)

    # Esse teste server para testar o ppassword-change
    def test_password_change(self):
        response = self.client.get(reverse('password-change'))
        self.assertEquals(response.status_code, 302)


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
        response = self.client.post(self.register_url1, data)
        self.assertEquals(response.status_code, 200)


