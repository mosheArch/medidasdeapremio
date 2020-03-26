from django.urls import path, include
from .views import ViewMedidaApremio, ViewListarMedidasApremio, ViewUpdateMedidasApremio, ViewDeleteMedidasApremio

urlpatterns = [
    path('creamedida/', ViewMedidaApremio.as_view(), name="crearM"),
    path('listamedida/', ViewListarMedidasApremio.as_view(), name= "listarM"),
    path('actualizarmedida/<int:pk>', ViewUpdateMedidasApremio.as_view(), name= "actualizarM"),
    path('eliminarmedida/<int:pk>', ViewDeleteMedidasApremio.as_view(), name= "eliminarM")
]

