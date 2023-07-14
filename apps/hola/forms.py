from django import forms

from apps.hola.models import Persona


# class FormularioPersona(forms.ModelForm):
#     email = forms.CharField(max_length=50)
#     class Meta:
#         model = Persona
#         fields = (
#             'nombre',
#             'edad',
#             'fecha',
#             'compania',
#             'hobbies',
#         )


class FormularioPersona(forms.Form):
    nombre = forms.CharField(max_length=100)
    website = forms.URLField()
    