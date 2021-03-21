from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/(?P<slug>[\w_-]+)/$', views.CreateCarrinhoItemView.as_view(), name='criar_carrinhoitem'),
]
