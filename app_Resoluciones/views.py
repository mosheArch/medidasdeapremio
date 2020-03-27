from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .models import Resoluciones
from .formResoluciones import FormResoluciones


class ViewCreateResolucion(CreateView):
    model = Resoluciones
    template_name = 'resoluciones/crearResolucion.html'
    form_class = FormResoluciones
    success_url = '/listarresolucion'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.save()
        return super(ViewCreateResolucion, self).form_valid(form)


class ViewListResoluciones(ListView):
    model = Resoluciones
    template_name = 'resoluciones/listarResolucion.html'
    context_object_name = 'listarResoluciones'


class ViewUpdateResoluciones(UpdateView):
    model = Resoluciones
    template_name = 'resoluciones/crearResolucion.html'
    form_class = FormResoluciones
    success_url = '/listarresolucion'


class ViewDeleteResolucion(DeleteView):
    model = Resoluciones
    template_name = 'resoluciones/deleteResolucion.html'
    success_url = '/listarresolucion'
