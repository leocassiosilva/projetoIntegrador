from django.urls import path, include
from rest_framework import routers

from pedidos.views import test
from .api.viewsets import UsuarioViewSet
from .views import CriarUsuario, UserLogin, LogoutView, IndexView, UpdateUsuario, PasswordReset, PasswordResetDone, \
    PasswordResetConfirm, PasswordResetCompleteView, PasswordChange, CriarVendedor

router = routers.DefaultRouter()
router.register(r'users', UsuarioViewSet)


urlpatterns = [
    path('cadastrar/', CriarUsuario.as_view(), name='cadastrar'),
    path('vendedor/', CriarVendedor.as_view(), name='cadastrar_vendedor'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    #path('index/', IndexView.as_view(), name='index'),
    path('atualizar/<int:pk>/', UpdateUsuario.as_view(), name='atualizar'),
    path('password-reset/', PasswordReset.as_view(), name='password-reset'),
    path('password_reset/done/', PasswordResetDone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_reset_complete'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-change/', PasswordChange.as_view(), name='password-change'),
    path('', include(router.urls)),

]
