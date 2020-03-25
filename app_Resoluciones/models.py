from django.db import models
from app_MediosImpugnacion.models import MediosImpugnacion


class Resoluciones(models.Model):

    no_expediente = models.CharField(max_length=255, null=False)
    fecha_resolucion = models.DateField(auto_now=False)
    puntos_resolucion = models.TextField(max_length=255, null=False)
    sentido_resolucion = models.TextField(max_length=255, null=False)
    multa = models.IntegerField(null=False)
    medioImpugnacion = models.ForeignKey(MediosImpugnacion, on_delete=models.CASCADE)
