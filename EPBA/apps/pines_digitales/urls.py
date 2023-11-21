from django.urls import path
from . import views

app_name = 'pines_digitales_app'

urlpatterns = [
    path('pines_digitales',views.pines_digitales.as_view(),name = 'pines_digitales'),
    path('pines_digitales/ejemplo-1',views.ejemplo1.as_view(),name = 'ejemplo1'),
    path('pines_digitales/ejemplo-2',views.ejemplo2.as_view(),name = 'ejemplo2'),
    path('pines_digitales/ejemplo-3',views.ejemplo3.as_view(),name = 'ejemplo3'),
    path('pines_digitales/ejemplo-4',views.ejemplo4.as_view(),name = 'ejemplo4'),
    path('pines_digitales/ejemplo-5',views.ejemplo5.as_view(),name = 'ejemplo5'),
    path('pines_digitales/ejemplo-6',views.ejemplo6.as_view(),name = 'ejemplo6'),
]