from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, RedirectView, TemplateView, UpdateView
from rolepermissions.roles import assign_role

from accounts.forms import CustomUsuarioCriarForm
from accounts.models import CustomUsuario, TipoUsuarios


class CriarUsuario(SuccessMessageMixin, CreateView):
    model = CustomUsuario
    form_class = CustomUsuarioCriarForm
    template_name = 'accounts/new_user.html'
    success_url = '/accounts/login'
    success_message = 'Bem vindo! Faça login para começar '

    def save(self,request, commit=True, ):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]

        if commit:
            user.save()
            assign_role(user, 'cliente')
        else:
            messages.error("Formulario Invalido")
        return user



class CriarVendedor(SuccessMessageMixin, CreateView):
    model = CustomUsuario
    form_class = CustomUsuarioCriarForm
    template_name = 'accounts/new_vendedor.html'
    success_url = '/accounts/login'
    success_message = 'Bem vindo! Faça login para começar '


class UpdateUsuario(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CustomUsuario
    fields = ('first_name', 'last_name', 'telefone', 'cep', 'cidade', 'rua', 'bairro', 'logadouro',
              'numero')
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('home')


class UserLogin(SuccessMessageMixin, LoginView):
    template_name = 'accounts/login.html'
    success_url = 'accounts/index'


class LogoutView(LoginRequiredMixin, RedirectView):
    url = '/accounts/login/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(self, request, *args, **kwargs)


class IndexView(TemplateView):
    template_name = 'accounts/index.html'


class PasswordReset(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password-reset.html'


class PasswordResetDone(SuccessMessageMixin, PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'


class PasswordResetConfirm(SuccessMessageMixin, PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'


class PasswordResetCompleteView(SuccessMessageMixin, PasswordResetCompleteView):
    success_message = 'Senha Alterada com sucesso!'
    template_name = 'accounts/login.html'


class PasswordChange(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = '/accounts/index'
    success_message = "Senha alterada com sucesso!"
