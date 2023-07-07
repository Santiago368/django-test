from django.urls import path

from .views import hola_mundo
# from apps.hola.views import hola_mundo
# from apps.hola import views


urlpatterns = [
    path('hola', hola_mundo),
]
