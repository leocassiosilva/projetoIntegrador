from django.shortcuts import render
from django.views.generic import TemplateView

from accounts.models import CustomUsuario


def index(request):
    return render(request, 'index.html')
