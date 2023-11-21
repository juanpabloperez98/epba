from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class proyecto3(TemplateView):
    template_name = "proyectos/proyecto3/proyecto3.html"