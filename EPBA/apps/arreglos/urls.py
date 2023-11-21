from django.urls import path
from . import views

app_name = 'arreglos_app'

urlpatterns = [
    path('arreglos',views.arreglos.as_view(),name = 'arreglos'),
    path('arreglos/ejemplo-1',views.ejemplo1.as_view(),name = 'ejemplo1'),
    path('arreglos/ejemplo-2',views.ejemplo2.as_view(),name = 'ejemplo2'),
    path('arreglos/ejemplo-3',views.ejemplo3.as_view(),name = 'ejemplo3'),
    path('arreglos/ejemplo-4',views.ejemplo4.as_view(),name = 'ejemplo4'),
    path('arreglos/ejemplo-5',views.ejemplo5.as_view(),name = 'ejemplo5'),
    path('arreglos/ejemplo-6',views.ejemplo6.as_view(),name = 'ejemplo6'),
]