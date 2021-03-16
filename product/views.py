from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # UpdateView
from rolepermissions.checkers import has_permission
from rolepermissions.mixins import HasRoleMixin

from .forms import ProductForm
from .models import Product, Category
from django.urls import reverse_lazy, reverse


# Create
class CategoryCreate(CreateView):
    model = Category
    fields = ['name']
    template_name = 'register/formCategory.html'
    success_url = reverse_lazy('index')


class ProductCreate(HasRoleMixin, CreateView):
    model = Product
    fields = ['name', 'category', 'quantity', 'description', 'price', 'image']
    template_name = 'register/formProduct.html'
    allowed_roles = 'vendedor'

    def form_valid(self, form):
        product = form.save(commit=False)
        product.id_usuario = self.request.user
        product.save()
        return super(ProductCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('produtos_list')


class ProductListView(HasRoleMixin, ListView):
    template_name = 'register/product_list.html'
    model = Product
    allowed_roles = 'vendedor'

    def get_queryset(self):
        produtos = Product.objects.order_by('name').filter(id_usuario=self.request.user)
        print(produtos)
        return produtos


class ProductUpdateView(HasRoleMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'register/product_update.html'
    allowed_roles = 'vendedor'

    def get_success_url(self):
        return reverse('produtos_lista')


class ProductDeleteView(HasRoleMixin, DeleteView):
    model = Product
    template_name = 'register/product_delete.html'
    allowed_roles = 'vendedor'

    def get_success_url(self):
        return reverse('produtos_lista')


class ProductDetailView(DetailView):
    model = Product
    # fields = [colocar fields]


class ProductListViewProdutos(ListView):
    template_name = 'register/produtos_list.html'
    model = Product

    def get_queryset(self):
        produtos = Product.objects.all()
        #produtos = Product.objects.order_by('name').filter(id_usuario=self.request.user)
        print(produtos)
        return produtos
