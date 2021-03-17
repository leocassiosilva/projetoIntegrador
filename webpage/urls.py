from .views import home, IndexView
from django.urls import path, include

urlpatterns = [
    path('', home, name='home'),
    path('index/', IndexView.as_view(), name='index'),
]
