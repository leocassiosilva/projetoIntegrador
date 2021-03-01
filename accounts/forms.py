from django.contrib.auth.forms import UserCreationForm

from .models import CustomUsuario


class CustomUsuarioCriarForm(UserCreationForm):
    class Meta:
        model = CustomUsuario
        fields = (
            'username', 'first_name', 'last_name', 'tipo', 'telefone', 'cep', 'cidade', 'rua', 'bairro', 'logadouro',
            'numero')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]

        if commit:
            user.save()
        return user
