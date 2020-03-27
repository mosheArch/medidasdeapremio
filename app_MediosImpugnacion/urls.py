from django.urls import path
from .views import ViewCrearMediosImpugnacion, ViewListarMediosImpugnacion, ViewUpdateMediosImpugnacion, ViewDeleteMedioImpugnacion
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('crearmedio/',login_required(ViewCrearMediosImpugnacion.as_view()), name="crearMedio"),
    path('listarmedio/', login_required(ViewListarMediosImpugnacion.as_view()), name= "listarMedio"),
    path('actualizarmedio/<int:pk>', login_required(ViewUpdateMediosImpugnacion.as_view()), name= "actualizarMedio"),
    path('eliminarmedio/<int:pk>', login_required(ViewDeleteMedioImpugnacion.as_view()), name= "eliminarMedio")
]

