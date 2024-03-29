from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models


class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email é obrigatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')
        return self._create_user(email, password, **extra_fields)


class CustomUsuario(AbstractUser):
    first_name = models.CharField(verbose_name=('Nome'), max_length=100, blank=False,
                                  help_text=('Nome é um campo obrigatorio'))
    last_name = models.CharField(verbose_name=('Sobrenome'), max_length=100, blank=False,
                                 help_text=('Sobrenome é obrigatorio'))
    email = models.EmailField('E-mail', unique=True)
    telefone = models.CharField('Telefone', max_length=15)
    cep = models.CharField('Cep', max_length=20, blank=True, null=True)
    cidade = models.CharField('Cidade', max_length=100, blank=True, null=True)
    rua = models.CharField('Rua', max_length=100, blank=True, null=True)
    bairro = models.CharField('Bairro', max_length=100, blank=True, null=True)
    logadouro = models.CharField('Logadouro', max_length=100, blank=True, null=True)
    numero = models.CharField('Numero', max_length=30, blank=True, null=True)
    nome_banca = models.CharField(verbose_name=('NomeBanca'), max_length=100, blank=False,
                                  help_text=('Nome da Banca é um campo obrigatorio'))
    image = models.ImageField(
        'Imagem', upload_to='Cliente', blank=True, null=True)
    is_staff = models.BooleanField("Membro da equipe", default=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    class Meta:
        db_table = "usuario"
        managed = True

    objects = UsuarioManager()
