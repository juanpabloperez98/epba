from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class proyecto4(TemplateView):
    template_name = "proyectos/proyecto4/proyecto4.html"