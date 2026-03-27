from django.contrib import admin
from django.urls import path, include
from inicio.views import inicio
from usuarios.views import login,cadastro

urlpatterns = [
    path("", inicio),
    path("admin/", admin.site.urls),
    path("usuarios/", include(arg="usuarios.urls"))
]

