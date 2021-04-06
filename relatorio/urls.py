from django.urls import path, include
from .views import GeneratePdf,TemplateRelatorio

urlpatterns = [
    path('produtos/', GeneratePdf.as_view(), name='gerar_relatorio'),
    path('baixar/', TemplateRelatorio.as_view(), name='baixar_relatorio'),
]