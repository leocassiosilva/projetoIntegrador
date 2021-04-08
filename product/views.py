from itertools import product
from secrets import token_urlsafe

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Sum
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import generic
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # UpdateView
from rolepermissions.checkers import has_permission
from rolepermissions.mixins import HasRoleMixin
from django.db import models

from .forms import ProductForm, ProductFormUpdate
from .models import Product, Category, Medida
from django.urls import reverse_lazy, reverse


class CategoryCreate(CreateView):
    model = Category
    fields = ['name']
    template_name = 'register/formCategory.html'
    success_url = reverse_lazy('cadastrarCategoria')


class MedidaCreate(CreateView):
    model = Medida
    fields = ['name']
    template_name = 'register/formMedida.html'
    success_url = reverse_lazy('cadastrarMedida')


class ProductCreate(LoginRequiredMixin, HasRoleMixin, CreateView):
    model = Product
    fields = ['name', 'category', 'medida', 'quantity', 'description', 'price', 'data_entrega', 'image']
    template_name = 'register/formProduct.html'
    allowed_roles = 'vendedor'
    success_url = '/product/lista'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = list(Category.objects.all())
        context['medidas'] = list(Medida.objects.all())
        return context

    def form_valid(self, form):
        product = form.save(commit=False)
        product.id_usuario = self.request.user
        token = token_urlsafe(16)
        product.slug = token
        product.save()
        return super(ProductCreate, self).form_valid(form)


class ProductListView(LoginRequiredMixin, HasRoleMixin, generic.ListView):
    template_name = 'register/product_list.html'
    model = Product
    allowed_roles = 'vendedor'
    paginate_by = 10

    def get_queryset(self):
        # produtos = Product.objects.all()
        produtos = Product.objects.order_by('name').filter(id_usuario=self.request.user)
        return produtos


class ProductUpdateView(LoginRequiredMixin, HasRoleMixin, UpdateView):
    model = Product
    form_class = ProductFormUpdate
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
    paginate_by = 6

    def get_queryset(self):
        produtos = Product.objects.annotate(country_quantity=Sum('quantity')).filter(status=0,
                                                          country_quantity__gt=0)
        return produtos


class ProdutoSeach(ListView):
    model = Product
    template_name = 'register/produtos_list.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = Product.objects.all()
        term = self.request.GET.get('term', '')
        if term:
            queryset = queryset.filter(
                models.Q(name__icontains=term) | models.Q(category__name__icontains=term)
            )
        return queryset


def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'register/produtos_list.html', context)


class ProductVendedorListViewProdutos(ListView):
    template_name = 'register/vendedor_produtos_list.html'
    model = Product
    paginate_by = 6

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)
        produtos = Product.objects.annotate(country_quantity=Sum('quantity')).filter(id_usuario=pk, status=0,
                                                                                     country_quantity__gt=0)
        context['produtos'] = list(produtos)
        print(produtos)
        return context
