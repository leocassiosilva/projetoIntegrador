from rest_framework import viewsets

from accounts.api.serializers import UsuarioSerializer
from accounts.models import CustomUsuario


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = CustomUsuario.objects.all()
    serializer_class = UsuarioSerializer
