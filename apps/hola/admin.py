import re 

from django.contrib import admin

from apps.hola import models


admin.site.register(models.Persona)
admin.site.register(models.Compania)
admin.site.register(models.Certificado)
admin.site.register(models.Hobbies)