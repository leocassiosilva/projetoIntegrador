from django.urls import path
from . import views

urlpatterns = [
    path('finalizando/', views.checkout, name='pedidos'),
    path('meusPedidos/', views.pedidoList, name='meus_Pedidos'),
    path('detalhe/<int:pk>/', views.detailPeddio, name='pedidos_detalhe'),
    path('atualizar/<int:pk>/', views.pedidoUpdate, name='pedidos_update'),

]
