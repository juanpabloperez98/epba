from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class proyecto2(TemplateView):
    template_name = "proyectos/proyecto2/proyecto2.html"