from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),  # Ruta para "/"
    path('home', home, name='home'),  # Ruta para "/home"
]