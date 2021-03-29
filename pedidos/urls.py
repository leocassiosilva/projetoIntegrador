from django.urls import path
from . import views

urlpatterns = [
    path('finalizando/', views.checkout, name='pedidos'),
    path('meusPedidos/', views.pedidoList, name='meus_Pedidos'),
    path('detalhe/<int:pk>/', views.pedidoDetail, name='pedidos_detalhe'),

]