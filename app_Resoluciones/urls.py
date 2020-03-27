from django.urls import path
from .views import ViewCreateResolucion, ViewListResoluciones, ViewUpdateResoluciones, ViewDeleteResolucion

urlpatterns = [
    path('crearresolucion/',ViewCreateResolucion.as_view(), name="crearResolucion"),
    path('listarresolucion/', ViewListResoluciones.as_view(), name= "listarResolucion"),
    path('actualizarresolucion/<int:pk>', ViewUpdateResoluciones.as_view(), name= "actualizarResolucion"),
    path('eliminarresolucion/<int:pk>', ViewDeleteResolucion.as_view(), name= "eliminarResolucion")
]

