from django.views.generic.edit import CreateView #UpdateView
from .models import Product, Category
from django.urls import reverse_lazy

# Create
class CategoryCreate(CreateView):

    model = Category
    fields = ['name']
    template_name = 'register/form.html'
    success_url = reverse_lazy('index')

class ProductCreate(CreateView):

    model = Product
    fields = ['name', 'category', 'quantity', 'description', 'price', 'image']
    template_name = 'register/form.html'
    success_url = reverse_lazy('index')