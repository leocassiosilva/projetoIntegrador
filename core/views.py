from django.shortcuts import render
from django.http import HttpResponse

from accounts.models import CustomUsuario


def index(request):
    print(CustomUsuario.groups.filter(name='Produtor'))
    return render(request, 'index.html')