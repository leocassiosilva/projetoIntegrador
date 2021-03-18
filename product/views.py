from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import generic
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # UpdateView
from rolepermissions.checkers import has_permission
from rolepermissions.mixins import HasRoleMixin

from .forms import ProductForm
from .models import Product, Category
from django.urls import reverse_lazy, reverse


class CategoryCreate(CreateView):
    model = Category
    fields = ['name']
    template_name = 'register/formCategory.html'
    success_url = reverse_lazy('index')


class ProductCreate(LoginRequiredMixin, HasRoleMixin, CreateView):
    model = Product
    fields = ['name', 'category', 'quantity', 'description', 'price', 'image']
    template_name = 'register/formProduct.html'
    allowed_roles = 'vendedor'
    success_url = '/product/lista'

    def form_valid(self, form):
        product = form.save(commit=False)
        product.id_usuario = self.request.user
        product.save()
        print("d")
        return super(ProductCreate, self).form_valid(form)


class ProductListView(LoginRequiredMixin, HasRoleMixin, generic.ListView):
    template_name = 'register/product_list.html'
    model = Product
    allowed_roles = 'vendedor'

    def get_queryset(self):
        # produtos = Product.objects.all()
        produtos = Product.objects.order_by('name').filter(id_usuario=self.request.user)
        print(self.request.user)
        return produtos


class ProductUpdateView(LoginRequiredMixin, HasRoleMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'register/product_update.html'
    allowed_roles = 'vendedor'

    def get_success_url(self):
        return reverse('produtos_lista')


class ProductDeleteView(LoginRequiredMixin, HasRoleMixin, DeleteView):
    model = Product
    template_name = 'register/product_delete.html'
    allowed_roles = 'vendedor'

    def get_success_url(self):
        return reverse('produtos_lista')


class ProductDetailView(LoginRequiredMixin, HasRoleMixin, DetailView):
    model = Product
    # fields = [colocar fields]
    allowed_roles = 'vendedor'


class ProductListViewProdutos(ListView):
    template_name = 'register/produtos_list.html'
    model = Product

    def get_queryset(self):
        produtos = Product.objects.all()
        return produtos


class ProdutoSeach(ListView):
    model = Product
    template_name = 'register/produtos_list.html'

    def get_queryset(self):
        term = self.request.GET.get('term')
        print(term)
        produtos = Product.objects.filter(name=term)
        print(produtos)
        return produtos


def autoCompleteProdutos(request):
    if request.is_ajax():
        term = request.GET.get('search')
        queryset = Product.objects.filter(name=term)
        response_content = list(queryset.values());
        return JsonResponse(response_content, safe=False)
