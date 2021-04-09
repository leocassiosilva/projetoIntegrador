from rest_framework import viewsets

from checkout.api.serializers import CarrinhoItemSerializer
from checkout.models import CarrinhoItem


class CarrinhoItemViewSet(viewsets.ModelViewSet):
    queryset = CarrinhoItem.objects.all()
    serializer_class = CarrinhoItemSerializer


