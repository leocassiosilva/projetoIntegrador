from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField('Nome', max_length=100)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name

class Medida(models.Model):
    name = models.CharField('Nome', max_length=100)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Medida'
        verbose_name_plural = 'Medidas'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    category = models.ForeignKey('product.Category', verbose_name='Categoria', on_delete=models.CASCADE)
    medida = models.ForeignKey('product.Medida', verbose_name='Medida', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    description = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    image = models.ImageField(
        'Imagem', upload_to='products', blank=True, null=True
    )
    id_usuario = models.ForeignKey("accounts.CustomUsuario", on_delete=models.CASCADE, db_column="id_usuario")
    data_entrega = models.DateField(blank=True, null=True, db_column="data_entrega")

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('criar_carrinhoitem', kwargs={'slug': self.slug})