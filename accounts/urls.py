from django.urls import path, include

from .views import CriarUsuario

urlpatterns = [
    path('cadastrar/', CriarUsuario.as_view(), name='cadastrar'),
]
