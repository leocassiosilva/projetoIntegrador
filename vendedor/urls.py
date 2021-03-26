from django.urls import path, re_path
from .views import VendedoresListView

urlpatterns = [
    path('bancas/', VendedoresListView.as_view(), name='vendedor_banca'),

]
