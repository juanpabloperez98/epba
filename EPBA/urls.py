from django.contrib import admin
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('',include('apps.main.urls')),
    re_path('',include('apps.arreglos.urls')),
    re_path('',include('apps.ciclos.urls')),
    re_path('',include('apps.clases.urls')),
    re_path('',include('apps.condicionales.urls')),
    re_path('',include('apps.funciones.urls')),
    re_path('',include('apps.matrices.urls')),
    re_path('',include('apps.operadores.urls')),
    re_path('',include('apps.pines_analogos.urls')),
    re_path('',include('apps.pines_digitales.urls')),
    re_path('',include('apps.pwm.urls')),
    re_path('',include('apps.variables.urls')),
    re_path('',include('apps.vcp.urls')),
    re_path('',include('apps.proyecto1.urls')),
    re_path('',include('apps.proyecto2.urls')),
    re_path('',include('apps.proyecto3.urls')),
    re_path('',include('apps.proyecto4.urls')),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)