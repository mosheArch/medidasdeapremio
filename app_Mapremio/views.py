from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from .models import MedidasdeApremio
from .form_MedidaApremio import MedidasdeApremioForm

class ViewMedidaApremio(CreateView):
    model = MedidasdeApremio
    template_name = 'medidas_apremio/crear_medida.html'
    form_class = MedidasdeApremioForm
    success_url = '/listamedida'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.save()
        return super(ViewMedidaApremio, self).form_valid(form)


class ViewListarMedidasApremio(ListView):
    model = MedidasdeApremio
    template_name = 'medidas_apremio/listarMedidasApremio.html'
    context_object_name = 'listarMedidasApremio'
    ordering = ['-cantidad']


class ViewUpdateMedidasApremio(UpdateView):
    model = MedidasdeApremio
    template_name = 'medidas_apremio/crear_medida.html'
    form_class = MedidasdeApremioForm
    success_url = '/listamedida'


class ViewDeleteMedidasApremio(DeleteView):
    model = MedidasdeApremio
    template_name = 'medidas_apremio/deleteMedida.html'
    success_url = '/listamedida'

