from django.urls import path, include
from .views import GeneratePdf

urlpatterns = [
    path('produtos/', GeneratePdf.as_view(), name='gerar_relatorio'),

]