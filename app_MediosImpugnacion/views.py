from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from .models import MediosImpugnacion
from .form_medios_impugnacion import FormMediosImpugnacion


class ViewCrearMediosImpugnacion(CreateView):
    model = MediosImpugnacion
    template_name = 'medios_impugnacion/crearMedioImpugnacion.html'
    form_class = FormMediosImpugnacion
    success_url = '/listarmedio'


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.save()
        return super(ViewCrearMediosImpugnacion, self).form_valid(form)



class ViewListarMediosImpugnacion(ListView):
    model = MediosImpugnacion
    template_name = 'medios_impugnacion/listaMedioImpugnacion.html'
    context_object_name = 'listarMedioImpugnacion'


class ViewUpdateMediosImpugnacion(UpdateView):
    model = MediosImpugnacion
    template_name = 'medios_impugnacion/crearMedioImpugnacion.html'
    form_class = FormMediosImpugnacion
    success_url = '/listarmedio'

class ViewDeleteMedioImpugnacion(DeleteView):
    model = MediosImpugnacion
    template_name = 'medios_impugnacion/deleteMedio.html'
    success_url = '/listarmedio'
