from django.urls import path, re_path
from . import views

urlpatterns = [
<<<<<<< HEAD
    re_path('adicionar/(?P<slug>[\w_-]+)/$', views.CreateCarrinhoItemView.as_view(), name='criar_carrinhoitem'),
=======
    re_path('^adicionar/(?P<slug>[\w_-]+)/$', views.CreateCarrinhoItemView, name='criar_carrinhoitem'),
>>>>>>> 0d12ffd15b79bc3954a247b104a6a974c9bd6c93
]
