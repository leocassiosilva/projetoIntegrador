from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render


# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, RedirectView, TemplateView, UpdateView

from accounts.forms import CustomUsuarioCriarForm
from accounts.models import CustomUsuario, TipoUsuarios


class CriarUsuario(SuccessMessageMixin, CreateView):
    model = CustomUsuario
    form_class = CustomUsuarioCriarForm
    template_name = 'accounts/new_user.html'
    success_url = '/accounts/login'
    success_message = 'Bem vindo! Faça login para começar '

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipos'] = list(TipoUsuarios.objects.all())
        return context


class UpdateUsuario(SuccessMessageMixin, UpdateView):
    model = CustomUsuario
    fields = (
        'username', 'first_name', 'last_name', 'tipo', 'telefone', 'cep', 'cidade', 'rua', 'bairro', 'logadouro',
        'numero')
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('index')


class UserLogin(SuccessMessageMixin, LoginView):
    template_name = 'accounts/login.html'
    success_url = 'accounts/index'


class LogoutView(RedirectView):
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


class PasswordChange(SuccessMessageMixin, PasswordChangeView):
    template_name = 'accounts/password-change.html'
    success_url = '/accounts/index'
    success_message = "Senha alterada com sucesso!"
