from django.test import TestCase

# Create your tests here.
from ..models import CustomUsuario


class PessoaTestCase(TestCase):

    def setUp(self):
        CustomUsuario.objects.create(
            email="leocassio@gmail.com",
            username="leocassio@gmail.com",
            first_name="Leo",
            last_name="Silva",
            telefone="6565465465",
            cep="654454",
            cidade="natal",
            rua="sadsadsad",
            bairro="sdsdsd",
            logadouro="dsads",
            numero="sdadssasd",
            password="mnbvcxz987654321"
        )

    def teste_returno_str(self):
        p1 = CustomUsuario.objects.get(email='leocassio@gmail.com')
        self.assertEquals(p1.__str__(), 'leocassio@gmail.com')
