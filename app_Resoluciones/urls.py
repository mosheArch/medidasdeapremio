from django.urls import path
from .views import ViewCreateResolucion, ViewListResoluciones, ViewUpdateResoluciones, ViewDeleteResolucion
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('crearresolucion/',login_required(ViewCreateResolucion.as_view()), name="crearResolucion"),
    path('listarresolucion/', login_required(ViewListResoluciones.as_view()), name= "listarResolucion"),
    path('actualizarresolucion/<int:pk>', login_required(ViewUpdateResoluciones.as_view()), name= "actualizarResolucion"),
    path('eliminarresolucion/<int:pk>', login_required(ViewDeleteResolucion.as_view()), name= "eliminarResolucion")
]

