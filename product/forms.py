from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'medida', 'quantity', 'description', 'price', 'data_entrega', 'image']
