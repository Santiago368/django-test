from django.urls import path

from . import views
# from apps.hola.views import hola_mundo
# from apps.hola import views

app_name = 'hola'

urlpatterns = [
    path('hola1', views.hola_mundo),
    path('hola2', views.HolaMundo.as_view()),
    path('crear-persona1', views.CrearPersona.as_view(), name="crear"),
    path('crear-persona2', views.crear_persona),
    path('listar-personas', views.ListaPersonas.as_view(), name="timo"),
    path('actualizar-persona/<pk>', views.actualizar_persona)
]
