from django.urls import path
from . import views


urlpatterns = [
    path('apihello', views.HolaMundo.as_view())
]
