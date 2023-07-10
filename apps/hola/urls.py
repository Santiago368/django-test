from django.urls import path

from . import views
# from apps.hola.views import hola_mundo
# from apps.hola import views


urlpatterns = [
    path('hola1', views.hola_mundo),
    path('hola2', views.HolaMundo.as_view()),
    path('crear-persona1', views.CrearPersona.as_view()),
    path('crear-persona2', views.crear_persona),
    path('listar-personas', views.ListaPersonas.as_view())
]
