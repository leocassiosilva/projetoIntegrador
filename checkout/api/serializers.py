from rest_framework import serializers

from checkout.models import CarrinhoItem


class CarrinhoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarrinhoItem
        fields = '__all__'
