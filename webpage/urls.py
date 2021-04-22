from .views import home, IndexView, SomosView
from django.urls import path, include

urlpatterns = [
    path('', home, name='home'),
    path('index/', IndexView.as_view(), name='index'),
    path('sobre/', SomosView.as_view(), name='sobre'),
    path('product-chart/', IndexView.product_chart, name='productChart'),
]
