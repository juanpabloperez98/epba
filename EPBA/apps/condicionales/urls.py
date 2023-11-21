from django.urls import path
from . import views

app_name = 'condicionales_app'

urlpatterns = [
    path('condicionales',views.condicionales.as_view(),name = 'condicionales'),
    path('condicionales/ejemplo-1',views.ejemplo1.as_view(),name = 'ejemplo1'),
    path('condicionales/ejemplo-2',views.ejemplo2.as_view(),name = 'ejemplo2'),
    path('condicionales/ejemplo-3',views.ejemplo3.as_view(),name = 'ejemplo3'),
    path('condicionales/ejemplo-4',views.ejemplo4.as_view(),name = 'ejemplo4'),
    path('condicionales/ejemplo-5',views.ejemplo5.as_view(),name = 'ejemplo5'),
    path('condicionales/ejemplo-6',views.ejemplo6.as_view(),name = 'ejemplo6'),
]