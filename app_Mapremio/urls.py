from django.urls import path, include
from .views import ViewMedidaApremio, ViewListarMedidasApremio, ViewUpdateMedidasApremio, ViewDeleteMedidasApremio
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('creamedida/', login_required(ViewMedidaApremio.as_view()), name="crearM"),
    path('listamedida/', login_required(ViewListarMedidasApremio.as_view()), name= "listarM"),
    path('actualizarmedida/<int:pk>', login_required(ViewUpdateMedidasApremio.as_view()), name= "actualizarM"),
    path('eliminarmedida/<int:pk>', login_required(ViewDeleteMedidasApremio.as_view()), name= "eliminarM")
]

