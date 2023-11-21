from django.urls import path
from . import views

app_name = 'proyecto4_app'

urlpatterns = [
    path('proyecto4',views.proyecto4.as_view(),name = 'proyecto4'),
]