from django.urls import path
from . import views

app_name = 'proyecto1_app'

urlpatterns = [
    path('proyecto1',views.proyecto1.as_view(),name = 'proyecto1'),
]