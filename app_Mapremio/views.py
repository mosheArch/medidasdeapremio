from django.shortcuts import render
from django.views.generic import CreateView
from .models import MedidasdeApremio
from .form_MedidaApremio import EmpleadosForm

class ViewMedidaApremio(CreateView):
    model = MedidasdeApremio
    template_name = 'medidas_apremio/crear_medida.html'
    form_class = EmpleadosForm
    success_url = '/home'
    
    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.user = self.request.user
    #     self.object.save()
    #     return super(ViewMedidaApremio, self).form_valid(form)


