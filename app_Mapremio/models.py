from django.db import models
from django.contrib.auth.models import User


class MedidasdeApremio(models.Model):
    no_expediente = models.CharField(max_length=255, null=False, unique=True)
    motivos = models.TextField(max_length=255, null=False)
    SujetoObligado = models.CharField(max_length=255, null=False)
    nombreCortoSo = models.CharField(max_length=255, null=True)
    cantidad = models.IntegerField(null=False)
    tipoMedida = models.CharField(max_length=255, null=False)
    fechaEmision = models.DateField(auto_now=False)
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.no_expediente
