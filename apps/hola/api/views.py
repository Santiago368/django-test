from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HolaMundo(APIView): # a nuestra calzada
    def get(self, request, *args, **kwargs): # esto es un carril get
        data = {'mensaje': 'Hola mundo'}
        # la logica que ustedes quieran aca
        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs): # esto es un carril post
        data = {'mensaje': 'Hola mundo'}
        # la logica que ustedes quieran aca
        return Response(data, status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs): # esto es un carril delete
        data = {'mensaje': 'Hola mundo'}
        # la logica que ustedes quieran aca. enviamos un correo
        return Response(data, status=status.HTTP_200_OK)
    

# def hola_mundo(request):
#     data = {'mensaje': 'Hola mundo'}
#     return Response(data, status=status.HTTP_200_OK)

