from django.urls import path
from . import views

app_name = 'proyecto3_app'

urlpatterns = [
    path('proyecto3',views.proyecto3.as_view(),name = 'proyecto3'),
]