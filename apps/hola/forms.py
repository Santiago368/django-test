from django import forms

from apps.hola.models import Persona


class FormularioPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'