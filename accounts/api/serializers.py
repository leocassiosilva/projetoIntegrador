from rest_framework import serializers

from accounts.models import CustomUsuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUsuario
        fields = '__all__'
