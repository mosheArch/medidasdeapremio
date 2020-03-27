from django.urls import path
from .views import ViewCrearMediosImpugnacion, ViewListarMediosImpugnacion, ViewUpdateMediosImpugnacion, ViewDeleteMedioImpugnacion

urlpatterns = [
    path('crearmedio/',ViewCrearMediosImpugnacion.as_view(), name="crearMedio"),
    path('listarmedio/', ViewListarMediosImpugnacion.as_view(), name= "listarMedio"),
    path('actualizarmedio/<int:pk>', ViewUpdateMediosImpugnacion.as_view(), name= "actualizarMedio"),
    path('eliminarmedio/<int:pk>', ViewDeleteMedioImpugnacion.as_view(), name= "eliminarMedio")
]

