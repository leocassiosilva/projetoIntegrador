from django.shortcuts import render
from django.views.generic import TemplateView

from accounts.models import CustomUsuario


def home(request):
    return render(request, 'home.html')


class IndexView(TemplateView):
    template_name = 'index.html'