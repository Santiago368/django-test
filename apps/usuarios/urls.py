from django.urls import path

from . import views

app_name = "usuarios"

urlpatterns = [
    path('hola3', views.hola_mundo2, name="ejemplo"),
]
