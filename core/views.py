from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import TemplateView
from app_Mapremio.models import MedidasdeApremio
from app_MediosImpugnacion.models import MediosImpugnacion
from app_Resoluciones.models import Resoluciones


class PruebaView(TemplateView):
    template_name = 'home/home.html'


def Dashboard(request):
    mapremio = MedidasdeApremio.objects
    medios = MediosImpugnacion.objects
    resolucion = Resoluciones.objects
    cantidad = MedidasdeApremio.objects.aggregate(Sum('cantidad'))
    total = cantidad['cantidad__sum']

    dashboard = {'mapremio': mapremio, 'medios': medios, 'resolucion': resolucion, 'total': total}

    return render(request, 'home/home.html', dashboard)
