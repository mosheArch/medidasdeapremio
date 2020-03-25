from django.urls import path, include
from .views import ViewMedidaApremio

urlpatterns = [
    path('creamedida/', ViewMedidaApremio.as_view(), name="crearM")
]

