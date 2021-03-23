from django.test import TestCase, Client
from django.urls import reverse


# teste para view de cadastro de usuario
class UsuarioViewTestCase(TestCase):

    def test_cadastroUsuario(self):
        response = self.client.get(reverse('cadastrar'))
        self.assertEquals(response.status_code, 200)

    # Esse teste server para testar o password reset
    def test_password_reset_complete(self):
        response = self.client.get(reverse('password_reset_complete'))
        self.assertEquals(response.status_code, 200)

    # Esse teste server para testar o ppassword-change
    def test_password_change(self):
        response = self.client.get(reverse('password-change'))
        self.assertEquals(response.status_code, 302)
