from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.hola.models import Persona
from apps.hola.forms import FormularioPersona

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
    

class CrearPersona(CreateView):
    template_name = 'hola/persona/crear.html'
    model = Persona
    fields = '__all__'
    # success_url = '/listar-personas' # equivalente http://localhost:8000/
    success_url = reverse_lazy("usuarios:ejemplo")


class ListaPersonas(ListView):
    template_name = 'hola/persona/lista.html'
    model = Persona


def crear_persona(request):
    if request.method == 'GET':
        # ejecuto la logica de mi get, la que yo quiera
        contexto = {
            'form': FormularioPersona
        }
        return render(request, 'hola/persona/crear.html', contexto)
    elif request.method == 'POST':
        # ejecuto la logica de mi post, la que yo quiera
        form = FormularioPersona(request.POST)

        if form.is_valid():
            print("Es valido")
            # mi logica de guardado
            form.save()
            return HttpResponseRedirect("/listar-personas")
        else:
            print("No es valido", form.errors)
            contexto = {
                'form': form
            }
            return render(request, 'hola/persona/crear.html', contexto)
    
def actualizar_persona(request, pk=None):
    # if request.method == 'GET':
    #     # ejecuto la logica de mi get, la que yo quiera
    #     persona = Persona.objects.filter(pk=pk) # [ob1] queryset 

    #     if persona.exists():
    #         persona = persona.first()
    #         form = FormularioPersona(instance=persona)
    #         contexto = {
    #             'form': form
    #         }
    #         return render(request, 'hola/persona/update.html', contexto)
    #     else:
    #         return HttpResponse("404")
    # elif request.method == 'POST':
    #     persona = Persona.objects.filter(pk=pk).first()
    #     form = FormularioPersona(request.POST, instance=persona)

    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(reverse_lazy('hola:timo'))
    #     else:
    #         return render(request, 'hola/persona/update.html',{'form': form})
    if request.method == 'GET':
        persona = get_object_or_404(Persona, pk=pk)
        form = FormularioPersona(instance=persona)
        return render(request, 'hola/persona/update.html', {'form': form})
    
    elif request.method == 'POST':
        persona = get_object_or_404(Persona, pk=pk)
        form = FormularioPersona(request.POST, instance=persona)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('hola:timo'))
        else:
            return render(request, 'hola/persona/update.html',{'form': form})





    
