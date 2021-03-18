from django.test import TestCase
from django.urls import reverse


# Teste de unitario cadastro de usuario

# teste para view de cadastro de usuario
class UsuarioViewTestCase(TestCase):

    def test_cadastroUsuario(self):
        response = self.client.get(reverse('cadastrar'))
        self.assertEquals(response.status_code, 200)

    def test_login(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)

    # Esse teste foi proposital para que pudesse dar erro
    def test_password_reset(self):
        response = self.client.get(reverse('password-resetr'))
        self.assertEquals(response.status_code, 200)

    # Esse precisa fazer o login
    def test_update(self):
        response = self.client.get(reverse('atualizar/1/'))
        self.assertEquals(response.status_code, 200)

    # Esse teste server para testar o password reset
    def test_update(self):
        response = self.client.get(reverse('atualizar/1/'))
        self.assertEquals(response.status_code, 200)

    # path('password-reset/', PasswordReset.as_view(), name='password-reset'),
    # path('password_reset/done/', PasswordResetDone.as_view(), name='password_reset_done'),
