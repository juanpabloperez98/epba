from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class proyecto1(TemplateView):
    template_name = "proyectos/proyecto1/proyecto1.html"