from django.urls import path
from . import views

app_name = 'proyecto2_app'

urlpatterns = [
    path('proyecto2',views.proyecto2.as_view(),name = 'proyecto2'),
]