from django.urls import path, re_path, include
from rest_framework import routers

from . import views
from .api.viewsets import CarrinhoItemViewSet

router = routers.DefaultRouter()
router.register(r'checkout', CarrinhoItemViewSet)

urlpatterns = [
    re_path('^adicionar/(?P<slug>[\w_-]+)/$', views.create_cartitem, name='criar_carrinhoitem'),
    path('carrinho/', views.cart_item, name='cart_item'),
    path('', include(router.urls)),
]
