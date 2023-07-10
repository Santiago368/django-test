from django.shortcuts import render
from django.views.generic import TemplateView

from apps.hola.models import Persona


# esto es una vista basada en funcion FBV
def hola_mundo(request):
    print("Hola")
    return render(request, 'hola/hola.html')


# esto es una vista basada en clase CBV
class HolaMundo(TemplateView):
    template_name = 'hola/hola.html'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        personas = Persona.objects.all() # SELECT * FROM PERSONA
        contexto['personas'] = personas
        return contexto

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)