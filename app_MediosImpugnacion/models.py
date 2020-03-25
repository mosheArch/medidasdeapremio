from django.db import models
from app_Mapremio.models import MedidasdeApremio


class MediosImpugnacion(models.Model):
    choice_tipoMedioImpugnacion = {('Juicio de amparo', 'Juicio de amparo'),
                                   ('Juicio administrativo', 'Juicio administrativo')}

    no_expediente = models.CharField(max_length=255, null=False)
    fecha_emplazamiento = models.DateField(auto_now=False)
    tipo_medioImpugnacion = models.CharField(choices=choice_tipoMedioImpugnacion, default='Tipo', max_length=255,null=False)
    efecto_medioImpugnacion = models.TextField(max_length=255, null=False)
    comentarios = models.TextField(max_length=255, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    medidas_apremio = models.ForeignKey(MedidasdeApremio, on_delete=models.CASCADE)
