from django.contrib.auth.forms import UserCreationForm
from rolepermissions.roles import assign_role
from .models import CustomUsuario


class CustomUsuarioCriarForm(UserCreationForm):
    class Meta:
        model = CustomUsuario
        fields = (
            'username', 'first_name', 'last_name', 'telefone', 'cep', 'cidade', 'rua', 'bairro', 'logadouro',
            'numero')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]

        if commit:
            user.save()
            assign_role(user, 'cliente')
        return user


class FormVendedor(UserCreationForm):
    class Meta:
        model = CustomUsuario
        fields = (
            'username', 'first_name', 'last_name', 'telefone', 'cep', 'cidade', 'rua', 'bairro', 'logadouro',
            'numero')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]

        if commit:
            user.save()
            assign_role(user, 'produtor')
        return user
