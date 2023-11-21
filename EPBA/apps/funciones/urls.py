from django.urls import path
from . import views

app_name = 'funciones_app'

urlpatterns = [
    path('funciones',views.funciones.as_view(),name = 'funciones'),
    path('funciones/ejemplo-1',views.ejemplo1.as_view(),name = 'ejemplo1'),
    path('funciones/ejemplo-2',views.ejemplo2.as_view(),name = 'ejemplo2'),
    path('funciones/ejemplo-3',views.ejemplo3.as_view(),name = 'ejemplo3'),
    path('funciones/ejemplo-4',views.ejemplo4.as_view(),name = 'ejemplo4'),
    path('funciones/ejemplo-5',views.ejemplo5.as_view(),name = 'ejemplo5'),
    path('funciones/ejemplo-6',views.ejemplo6.as_view(),name = 'ejemplo6'),
]