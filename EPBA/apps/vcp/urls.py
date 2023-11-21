from django.urls import path
from . import views

app_name = 'vcp_app'

urlpatterns = [
    path('vcp',views.vcp.as_view(),name = 'vcp'),
    path('vcp/ejemplo-1',views.ejemplo1.as_view(),name = 'ejemplo1'),
    path('vcp/ejemplo-2',views.ejemplo2.as_view(),name = 'ejemplo2'),
    path('vcp/ejemplo-3',views.ejemplo3.as_view(),name = 'ejemplo3'),
    path('vcp/ejemplo-4',views.ejemplo4.as_view(),name = 'ejemplo4'),
    path('vcp/ejemplo-5',views.ejemplo5.as_view(),name = 'ejemplo5'),
    path('vcp/ejemplo-6',views.ejemplo6.as_view(),name = 'ejemplo6'),
]