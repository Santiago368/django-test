from django.shortcuts import render

# Create your views here.


def hola_mundo2(request):
    return render(request, 'hola/hola.html')