from django.contrib import admin

# Register your models here.
from .models import CustomUsuario, TipoUsuarios

admin.site.register(CustomUsuario)
admin.site.register(TipoUsuarios)