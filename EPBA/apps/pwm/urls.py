from django.urls import path
from . import views

app_name = 'pwm_app'

urlpatterns = [
    path('pwm',views.pwm.as_view(),name = 'pwm'),
    path('pwm/ejemplo-1',views.ejemplo1.as_view(),name = 'ejemplo1'),
    path('pwm/ejemplo-2',views.ejemplo2.as_view(),name = 'ejemplo2'),
    path('pwm/ejemplo-3',views.ejemplo3.as_view(),name = 'ejemplo3'),
    path('pwm/ejemplo-4',views.ejemplo4.as_view(),name = 'ejemplo4'),
    path('pwm/ejemplo-5',views.ejemplo5.as_view(),name = 'ejemplo5'),
    path('pwm/ejemplo-6',views.ejemplo6.as_view(),name = 'ejemplo6'),
]