from rest_framework import viewsets

from product.api.serializers import ProductSerializer
from product.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer