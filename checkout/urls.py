from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('^adicionar/(?P<slug>[\w_-]+)/$', views.create_cartitem, name='criar_carrinhoitem'),
]
