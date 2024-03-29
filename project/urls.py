"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from MiTiempo import views
from django.conf.urls import include, url

urlpatterns = [
    path('',views.paginaprincipal),
    path('MiTiempo/usercss.css', views.changecssuser),
    path('admin', admin.site.urls),
    url(r'^login', views.login_view),
    url(r'^logout', views.logout_view),
    url(r'^register$', views.register),
    path('info', views.informacion),
    path('municipios', views.listamunicipios),
    path('usuarios', views.listausuarios),
    path('municipios/<id>', views.mostrarinfmunicipio),
    path('<usuario>', views.pagusuario),
]
