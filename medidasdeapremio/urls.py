"""medidasdeapremio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views
from django.contrib.auth.decorators import login_required
from users.views import Login, salirUsuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(views.Dashboard), name="home"),
    path('', include('app_Mapremio.urls')),
    path('', include('app_MediosImpugnacion.urls')),
    path('', include('app_Resoluciones.urls')),
    path('accounts/login/', Login.as_view(), name='LogIn'),
    path('logout/', login_required(salirUsuario), name='salir'),
]
admin.site.site_header = 'Administrador de medisa de Apremio'
