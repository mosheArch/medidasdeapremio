from django.db import models
from app_Mapremio.models import MedidasdeApremio
from django.contrib.auth.models import User


class MediosImpugnacion(models.Model):
    choice_tipoMedioImpugnacion = {('Juicio de amparo', 'Juicio de amparo'),
                                   ('Juicio administrativo', 'Juicio administrativo')}

    no_expediente = models.CharField(max_length=255, null=False, unique=True)
    fecha_emplazamiento = models.DateField(auto_now=False)
    tipo_medioImpugnacion = models.CharField(choices=choice_tipoMedioImpugnacion, default='Tipo', max_length=255,null=False)
    efecto_medioImpugnacion = models.TextField(max_length=255, null=False)
    comentarios = models.TextField(max_length=255, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    medidas_apremio = models.ForeignKey(MedidasdeApremio, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.no_expediente
