from django.db import models

# Create your models here.


class Compania(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name
    

class Hobbies(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha = models.DateTimeField(null=True)
    compania = models.ForeignKey(
        Compania,
        on_delete=models.PROTECT, # CASCADE, PROTECT, SET_NULL
        null=True,
        blank=True
    ) # esto es como un listado
    hobbies = models.ManyToManyField(
        Hobbies,
        blank=True
    ) # no tiene on_delte parametro

    def __str__(self):
        return self.nombre
    

class Certificado(models.Model):
    name = models.CharField(max_length=50)
    persona = models.OneToOneField(
        Persona,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return self.name
    