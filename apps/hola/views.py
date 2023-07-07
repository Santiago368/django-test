from django.shortcuts import render

# Create your views here.


def hola_mundo(request):
    print("Hola")
    return render(request, 'hola/hola.html')
