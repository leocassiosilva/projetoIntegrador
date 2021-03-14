from django.db import models

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

class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    category = models.ForeignKey('product.Category', verbose_name='Categoria', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    description = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    image = models.ImageField(
        'Imagem', upload_to='products', blank=True, null=True
    )

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']

    def __str__(self):
        return self.name

