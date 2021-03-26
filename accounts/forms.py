from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rolepermissions.roles import assign_role
from .models import CustomUsuario


class CustomUsuarioCriarForm(UserCreationForm):
    class Meta:
        model = CustomUsuario
        fields = (
        'username', 'first_name', 'last_name', 'telefone', 'cep', 'cidade', 'rua', 'bairro', 'logadouro', 'numero')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]

        if commit:
            user.save()
            assign_role(user, 'cliente')
            data = {'usuario': user, }
            plain_text = render_to_string('accounts/emails/email.txt', data)
            html_email = render_to_string('accounts/emails/email.html', data)
            send_mail("Coma Bem - Seja Bem Vindo!",
                      plain_text,
                      "comabemrn@gmail.com",
                      ['{0}'.format(user)],
                      html_message=html_email
                      )
        return user


class FormVendedor(UserCreationForm):
    class Meta:
        model = CustomUsuario
        fields = (
        'username', 'first_name', 'last_name', 'telefone', 'cep', 'cidade', 'rua', 'bairro', 'logadouro', 'numero')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]

        if commit:
            user.save()
            assign_role(user, 'vendedor')
            data = {'usuario': user, }
            plain_text = render_to_string('accounts/emails/email.txt', data)
            html_email = render_to_string('accounts/emails/email.html', data)
            send_mail("Coma Bem - Seja Bem Vindo!",
                      plain_text,
                      "comabemrn@gmail.com",
                      ['{0}'.format(user)],
                      html_message=html_email
                      )
        return user
