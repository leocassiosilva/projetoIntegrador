from .views import IndexView
from django.urls import path, include

urlpatterns = [
    path('index', IndexView.as_view(), name='index'),
]