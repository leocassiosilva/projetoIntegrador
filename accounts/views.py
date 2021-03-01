from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

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
