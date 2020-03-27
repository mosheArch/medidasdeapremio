from django.contrib.auth.models import User
from django.db import models
from app_MediosImpugnacion.models import MediosImpugnacion


class Resoluciones(models.Model):
    choice_multa = {('Si', 'Si'),
                    ('No', 'No')}

    no_expediente = models.CharField(max_length=255, null=False, unique=True)
    fecha_resolucion = models.DateField(auto_now=False)
    puntos_resolucion = models.TextField(max_length=255, null=False)
    sentido_resolucion = models.TextField(max_length=255, null=False)
    multa = models.CharField(choices=choice_multa, max_length=10, null=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    medioImpugnacion = models.ForeignKey(MediosImpugnacion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.no_expediente
