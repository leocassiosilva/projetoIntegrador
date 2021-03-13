from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # UpdateView
from .models import Product, Category
from django.urls import reverse_lazy, reverse


# Create
class CategoryCreate(CreateView):
    model = Category
    fields = ['name']
    template_name = 'register/formCategory.html'
    success_url = reverse_lazy('index')


class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'category', 'quantity', 'description', 'price', 'image']
    success_url = reverse_lazy('index')


class ProductListView(ListView):
    template_name = 'register/product_list.html'
    model = Product

    def get_queryset(self):
        # produtos = Product.objects.all()
        produtos = Product.objects.order_by('nome').filter(id_usuario=self.request.user)
        print(produtos)
        return produtos


class ProductUpdateView(UpdateView):
    model = Product
    form_class = Product
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('produtos_lista')


class ProductDeleteView(DeleteView):
    model = Product

    def get_success_url(self):
        return reverse('produtos_lista')


class ProductDetailView(DetailView):
    model = Product
    #fields = [colocar fields]
