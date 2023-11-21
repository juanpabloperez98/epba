from django.urls import path
from . import views

app_name = 'variables_app'

urlpatterns = [
    path('variables',views.variables.as_view(),name = 'variables'),
    path('variables/ejemplo-1',views.ejemplo1.as_view(),name = 'ejemplo1'),
    path('variables/ejemplo-2',views.ejemplo2.as_view(),name = 'ejemplo2'),
    path('variables/ejemplo-3',views.ejemplo3.as_view(),name = 'ejemplo3'),
    path('variables/ejemplo-4',views.ejemplo4.as_view(),name = 'ejemplo4'),
    path('variables/ejemplo-5',views.ejemplo5.as_view(),name = 'ejemplo5'),
    path('variables/ejemplo-6',views.ejemplo6.as_view(),name = 'ejemplo6'),
]