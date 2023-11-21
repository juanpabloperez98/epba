from django.urls import path
from . import views

app_name = 'ciclos_app'

urlpatterns = [
    path('ciclos',views.ciclos.as_view(),name = 'ciclos'),
    path('ciclos/ejemplo-1',views.ejemplo1.as_view(),name = 'ejemplo1'),
    path('ciclos/ejemplo-2',views.ejemplo2.as_view(),name = 'ejemplo2'),
    path('ciclos/ejemplo-3',views.ejemplo3.as_view(),name = 'ejemplo3'),
    path('ciclos/ejemplo-4',views.ejemplo4.as_view(),name = 'ejemplo4'),
    path('ciclos/ejemplo-5',views.ejemplo5.as_view(),name = 'ejemplo5'),
    path('ciclos/ejemplo-6',views.ejemplo6.as_view(),name = 'ejemplo6'),
]