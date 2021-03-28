from django.urls import path
from . import views

urlpatterns = [
    path('finalizando/', views.checkout, name='pedidos'),
]