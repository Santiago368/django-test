from django.urls import path

from .views import hola_mundo, HolaMundo
# from apps.hola.views import hola_mundo
# from apps.hola import views


urlpatterns = [
    path('hola1', hola_mundo),
    path('hola2', HolaMundo.as_view()),
]
